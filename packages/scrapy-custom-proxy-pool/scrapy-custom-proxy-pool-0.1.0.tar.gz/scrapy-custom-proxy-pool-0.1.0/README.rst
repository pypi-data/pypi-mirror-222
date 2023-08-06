Scrapy Custom Proxy Pool
========================

A Scrapy middleware to manage a custom proxy pool and randomly choose a proxy for each request.

Installation
------------

.. code-block:: bash

    pip install scrapy-custom-proxy-pool

Usage
-----

In settings.py:

.. code-block:: python3

    DOWNLOADER_MIDDLEWARES = {
        # ...
        'scrapy_custom_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
        'scrapy_custom_proxy_pool.middlewares.BanDetectionMiddleware': 620,
        # ...
    }

    PROXY_POOL_ENABLED = True
    PROXY_POOL_SIZE = 10
    PROXY_POOL_COLLECTOR = 'myproject.collectors.MyCollector' 
    PROXY_POOL_COLLECTOR_ARGS = {}
    PROXY_POOL_REFRESH_INTERVAL = 60
    PROXY_POOL_PAGE_RETRY_TIMES = 5
    PROXY_POOL_TRY_WITH_HOST = True

Settings
--------

.. code-block:: python3

    PROXY_POOL_ENABLED - Enable/disable proxy pool (default: False)
    PROXY_POOL_SIZE - Max proxies in pool (default: 10)
    PROXY_POOL_COLLECTOR - Custom proxy collector path (required)
    PROXY_POOL_COLLECTOR_ARGS - Collector initialization arguments (default: {})
    PROXY_POOL_REFRESH_INTERVAL - Proxy refresh interval in secs (default: 60)
    PROXY_POOL_PAGE_RETRY_TIMES - Max retry times per page (default: 5)
    PROXY_POOL_TRY_WITH_HOST - Try requests without proxy (default: True)

Customization
-------------

Ban Detection Policy
~~~~~~~~~~~~~~~~~~~~

You can customize the ban detection policy:

.. code-block:: python3

    # myproject/policy.py
    from scrapy_custom_proxy_pool.policy import BanDetectionPolicy

    class MyPolicy(BanDetectionPolicy):
      # override response_is_ban and exception_is_ban

.. code-block:: python3

    # settings.py
    PROXY_POOL_BAN_POLICY = 'myproject.policy.MyPolicy'

Proxy Collector
~~~~~~~~~~~~~~~

You need to implement a custom proxy collector by subclassing ProxyCollector:

.. code-block:: python3

    from scrapy_custom_proxy_pool.collectors import ProxyCollector

    class MyCollector(ProxyCollector):

      def fetch_proxies(self, count):
        # return list of `Proxy` objects

License
-------

MIT