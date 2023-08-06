# -*- coding: utf-8 -*-

import requests
from requests.adapters import HTTPAdapter
from datetime import datetime, timedelta
from typing import List, Optional

from .base import Proxy, ProxyCollector


class QingguoProxyCollector(ProxyCollector):
    """
    A specific implementation of ProxyCollector that fetches proxies from Qingguo Cloud (qg.net).
    """

    def __init__(self, capacity: int, authkey: str, authpwd: Optional[str]=None,
                 area: Optional[str]=None, isp: Optional[str]=None):
        """
        Initialize the QingguoProxyCollector with capacity, authentication details and optional filtering parameters.
        :param capacity: Maximum number of proxies the collector can hold
        :param authkey: Authentication key provided by the Qingguo service
        :param authpwd: Authentication password provided by the Qingguo service (default is None)
        :param area: Optional filter for proxies by area (default is None)
        :param isp: Optional filter for proxies by ISP (default is None)
        """
        super().__init__(capacity)
        self._authkey = authkey
        self._authpwd = authpwd
        self.area = area if area else ''
        self.isp = isp if isp else ''

    def fetch_proxies(self, count) -> List[Proxy]:
        """
        Fetch a given number of proxies from Qingguo Cloud.
        :param count: The number of proxies to fetch
        :return: A list of fetched Proxy objects
        """
        s = requests.Session()
        s.mount('https://share.proxy.qg.net', HTTPAdapter(max_retries=5))
        
        r = s.get('https://share.proxy.qg.net/get', params={
            'key': self._authkey,
            'num': count,
            'format': 'json',
            'distinct': True,
            'area': self.area,
            'isp': self.isp,
            'pool': 1
        })
        
        resp = r.json()
        data = resp['data']
        proxies = []
        
        for item in data:
            host, port = item['server'].split(':')[:2]
            deadline = datetime.strptime(item['deadline'], '%Y-%m-%d %H:%M:%S') - timedelta(seconds=5)
            p = Proxy(host, port, deadline=deadline)
            
            if self._authkey and self._authpwd:
                p.username = self._authkey
                p.password = self._authpwd
                
            proxies.append(p)
            
        return proxies