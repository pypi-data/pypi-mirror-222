# -*- coding: utf-8 -*-

from __future__ import absolute_import
import logging

from scrapy.exceptions import CloseSpider, NotConfigured
from scrapy import signals
from scrapy.utils.misc import load_object
from twisted.internet import task
from .collector.base import Proxy, ProxyCollector

logger = logging.getLogger(__name__)


class ProxyPoolMiddleware(object):
    """
    Scrapy downloader middleware which choses a random proxy for each request.

    To enable it, add it and BanDetectionMiddleware
    to DOWNLOADER_MIDDLEWARES option::

        DOWNLOADER_MIDDLEWARES = {
            # ...
            'scrapy_custom_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
            'scrapy_custom_proxy_pool.middlewares.BanDetectionMiddleware': 620,
            # ...
        }

    It keeps track of dead and alive proxies and avoids using dead proxies.
    Proxy is considered dead if request.meta['_ban'] is True, and alive
    if request.meta['_ban'] is False; to set this meta key use
    BanDetectionMiddleware.

    Dead proxies are re-checked with a randomized exponential backoff.

    By default, all default Scrapy concurrency options (DOWNLOAD_DELAY,
    AUTHTHROTTLE_..., CONCURRENT_REQUESTS_PER_DOMAIN, etc) become per-proxy
    for proxied requests when RotatingProxyMiddleware is enabled.
    For example, if you set CONCURRENT_REQUESTS_PER_DOMAIN=2 then
    spider will be making at most 2 concurrent connections to each proxy.

    Settings:
    * ``PROXY_POOL_ENABLED`` - Flag to enable or disable the use of proxy pool.
      When False, proxy pool is disabled. Default: False.
    * ``PROXY_POOL_SIZE`` - Size of the proxy pool, i.e., maximum number of proxies
      that the pool should hold at any given time. Default: 10.
    * ``PROXY_POOL_COLLECTOR`` - Path to the class that is used to collect proxies.
      This class should be a subclass of `ProxyCollector`.
    * ``PROXY_POOL_COLLECTOR_ARGS`` - A dictionary containing arguments to be passed 
      to the collector class during initialization. Default: {} (empty dictionary).
    * ``PROXY_POOL_REFRESH_INTERVAL`` - proxies refresh interval in seconds,
      60 by default;
    * ``PROXY_POOL_PAGE_RETRY_TIMES`` - a number of times to retry
      downloading a page using a different proxy. After this amount of retries
      failure is considered a page failure, not a proxy failure.
      Think of it this way: every improperly detected ban cost you
      ``PROXY_POOL_PAGE_RETRY_TIMES`` alive proxies. Default: 5.
    * ``PROXY_POOL_TRY_WITH_HOST`` - When True, spider will try requests 
      that exceed PROXY_POOL_PAGE_RETRY_TIMES.
    """
    def __init__(self, collector: ProxyCollector, refresh_interval: int,
                 max_proxies_to_try: int, try_with_host: bool):
        self.collector = collector
        self.refresh_interval = refresh_interval
        self.max_proxies_to_try = max_proxies_to_try
        self.try_with_host = try_with_host


    @classmethod
    def from_crawler(cls, crawler):
        s = crawler.settings
        enabled = s.getbool('PROXY_POOL_ENABLED', False)
        if not enabled:
            raise NotConfigured()

        pool_size = s.get('PROXY_POOL_SIZE', 10)
        collector_path  = s.get('PROXY_POOL_COLLECTOR', None)
        collector_args  = s.get('PROXY_POOL_COLLECTOR_ARGS', {})
        if collector_path is None:
            raise NotConfigured()
        
        collector_args.update({'capacity': pool_size})
        collector_cls = load_object(collector_path)

        mw = cls(
            collector=collector_cls(**collector_args),
            refresh_interval=s.getfloat('PROXY_POOL_REFRESH_INTERVAL', 60),
            max_proxies_to_try=s.getint('PROXY_POOL_PAGE_RETRY_TIMES', 5),
            try_with_host=s.getbool('PROXY_POOL_TRY_WITH_HOST', True),
        )
        crawler.signals.connect(mw.engine_started,
                                signal=signals.engine_started)
        crawler.signals.connect(mw.engine_stopped,
                                signal=signals.engine_stopped)
        return mw

    def engine_started(self):
        self.refresh_proxies_task = task.LoopingCall(self.refresh_blacklist)
        self.refresh_proxies_task.start(self.refresh_interval, now=False)

    def engine_stopped(self):
        if self.refresh_proxies_task.running:
            self.refresh_proxies_task.stop()

    def process_request(self, request, spider):
        if 'proxy' in request.meta and not request.meta.get('_PROXY_POOL', False):
            return
        proxy = self.collector.get_proxy()
        if not proxy:
            self.collector.refresh_proxies()
            logger.info('Proxies refreshed.')
            self.refresh_blacklist()
            proxy = self.collector.get_proxy()

        if not proxy:
            if self.try_with_host:
                logger.info("Try to download with host ip.")
                request.meta.pop('proxy_source', None)
                request.meta.pop('proxy', None)
                request.meta.pop('download_slot', None)
                request.meta.pop('_PROXY_POOL', None)
                return
            else:
                raise CloseSpider()

        request.meta['proxy_source'] = proxy
        request.meta['proxy'] = proxy.uri
        request.meta['download_slot'] = self.get_proxy_slot(proxy)
        request.meta['_PROXY_POOL'] = True

        logger.debug('Proxy chosen: {}'.format(request.meta['proxy']))

    def refresh_blacklist(self):
        self.collector.clear_blacklist()
        logger.info('Blacklist is cleared.')

    def get_proxy_slot(self, proxy: Proxy):
        """
        Return downloader slot for a proxy.
        By default it doesn't take port in account, i.e. all proxies with
        the same hostname / ip address share the same slot.
        """
        return proxy.host

    def process_exception(self, request, exception, spider):
        return self._handle_result(request, spider)

    def process_response(self, request, response, spider):
        return self._handle_result(request, spider) or response

    def _handle_result(self, request, spider):
        proxy = request.meta.get('proxy_source', None)
        if not (proxy and request.meta.get('_PROXY_POOL', False)):
            return

        ban = request.meta.get('_ban', None)
        if ban is True:
            self.collector.blacklist_proxy(request.meta.get('proxy_source'))
            request.meta.pop('proxy_source', None)
            request.meta.pop('proxy', None)
            request.meta.pop('download_slot', None)
            request.meta.pop('_PROXY_POOL', None)
            return self._retry(request, spider)

    def _retry(self, request, spider):
        retries = request.meta.get('proxy_retry_times', 0) + 1
        max_proxies_to_try = request.meta.get('max_proxies_to_try',
                                              self.max_proxies_to_try)

        if retries <= max_proxies_to_try:
            logger.debug("Retrying %(request)s with another proxy "
                         "(failed %(retries)d times, "
                         "max retries: %(max_proxies_to_try)d)",
                         {'request': request, 'retries': retries,
                          'max_proxies_to_try': max_proxies_to_try},
                         extra={'spider': spider})
            retryreq = request.copy()
            retryreq.meta['proxy_retry_times'] = retries
            retryreq.dont_filter = True
            return retryreq
        else:
            logger.debug("Gave up retrying %(request)s (failed %(retries)d "
                         "times with different proxies)",
                         {'request': request, 'retries': retries},
                         extra={'spider': spider})

            if self.try_with_host:
                logger.debug("Try with host ip")
                req = request.copy()
                req.meta.pop('proxy_source', None)
                req.meta.pop('download_slot', None)
                req.meta.pop('_PROXY_POOL', None)
                req.meta['proxy'] = None
                req.dont_filter = True
                return req


class BanDetectionMiddleware(object):
    """
    Downloader middleware for detecting bans. It adds
    '_ban': True to request.meta if the response was a ban.

    To enable it, add it to DOWNLOADER_MIDDLEWARES option::

        DOWNLOADER_MIDDLEWARES = {
            # ...
            'scrapy_custom_proxy_pool.middlewares.BanDetectionMiddleware': 620,
            # ...
        }

    By default, client is considered banned if a request failed, and alive
    if a response was received. You can override ban detection method by
    passing a path to a custom BanDectionPolicy in
    ``PROXY_POOL_BAN_POLICY``, e.g.::

    PROXY_POOL_BAN_POLICY = 'myproject.policy.MyBanPolicy'

    The policy must be a class with ``response_is_ban``
    and ``exception_is_ban`` methods. These methods can return True
    (ban detected), False (not a ban) or None (unknown). It can be convenient
    to subclass and modify default BanDetectionPolicy::

        # myproject/policy.py
        from rotating_proxies.policy import BanDetectionPolicy

        class MyPolicy(BanDetectionPolicy):
            def response_is_ban(self, request, response):
                # use default rules, but also consider HTTP 200 responses
                # a ban if there is 'captcha' word in response body.
                ban = super(MyPolicy, self).response_is_ban(request, response)
                ban = ban or b'captcha' in response.body
                return ban

            def exception_is_ban(self, request, exception):
                # override method completely: don't take exceptions in account
                return None

    Instead of creating a policy you can also implement ``response_is_ban``
    and ``exception_is_ban`` methods as spider methods, for example::

        class MySpider(scrapy.Spider):
            # ...

            def response_is_ban(self, request, response):
                return b'banned' in response.body

            def exception_is_ban(self, request, exception):
                return None

    """
    def __init__(self, stats, policy):
        self.stats = stats
        self.policy = policy

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats, cls._load_policy(crawler))

    @classmethod
    def _load_policy(cls, crawler):
        policy_path = crawler.settings.get(
            'PROXY_POOL_BAN_POLICY',
            'scrapy_custom_proxy_pool.policy.BanDetectionPolicy'
        )
        policy_cls = load_object(policy_path)
        if hasattr(policy_cls, 'from_crawler'):
            return policy_cls.from_crawler(crawler)

        return policy_cls()

    def process_response(self, request, response, spider):
        is_ban = getattr(spider, 'response_is_ban',
                         self.policy.response_is_ban)
        ban = is_ban(request, response)
        request.meta['_ban'] = ban
        if ban:
            self.stats.inc_value("bans/status/%s" % response.status)
            if not len(response.body):
                self.stats.inc_value("bans/empty")
        return response

    def process_exception(self, request, exception, spider):
        is_ban = getattr(spider, 'exception_is_ban',
                         self.policy.exception_is_ban)
        ban = is_ban(request, exception)
        if ban:
            ex_class = "%s.%s" % (exception.__class__.__module__,
                                  exception.__class__.__name__)
            self.stats.inc_value("bans/error/%s" % ex_class)
        request.meta['_ban'] = ban