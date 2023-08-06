# -*- coding: utf-8 -*-

from collections import deque
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from typing import Optional, List, Set


class Proxy(object):
    """
    Proxy information with host, port and optional authentication.
    """

    def __init__(self, host: str, port: str, protocol: str='http',
                 username: Optional[str]=None, password: Optional[str]=None,
                 deadline: Optional[datetime]=None):
        """
        Initialize the proxy with given details. If username and password are provided, the proxy requires authentication.
        :param host: Proxy host address
        :param port: Proxy port number
        :param protocol: Proxy protocol (default is 'http')
        :param username: Proxy username for authentication (default is None)
        :param password: Proxy password for authentication (default is None)
        :param deadline: Expiry date and time of the proxy (default is None)
        """
        self.host = host
        self.port = port
        self.protocol = protocol
        self.username = username
        self.password = password
        self.deadline = deadline
    
    @property
    def uri(self):
        """
        Property method to get the full URI of the Proxy.
        :return: A string representing the full URI of the Proxy
        """
        auth = ''
        if self.username and self.password:
            auth = '%s:%s@' % (self.username, self.password)
        return '%s://%s%s:%s' % (self.protocol, auth, self.host, self.port)
    
    def __str__(self) -> str:
        return '%s://%s:%s' % (self.protocol, self.host, self.port)

    def __repr__(self) -> str:
        return str(self)


class ProxyCollector(ABC):
    """
    An abstract base class representing a Proxy collector. 
    This class can be subclassed to implement various strategies for collecting proxies.
    """

    def __init__(self, capacity: int):
        """
        Initialize the ProxyCollector with a given capacity.
        :param capacity: Maximum number of proxies the collector can hold
        """
        self._capacity = capacity
        self._proxies: deque[Proxy] = deque()
        self._blacklist: Set[Proxy] = set()

    @abstractmethod
    def fetch_proxies(self, count) -> List[Proxy]:
        """
        Abstract method to fetch a given number of proxies. 
        Subclasses must implement this method according to their specific proxy fetching strategy.
        :param count: The number of proxies to fetch
        :return: A list of fetched Proxy objects
        """
        pass

    def refresh_proxies(self) -> None:
        """
        Refresh the list of proxies by removing blacklisted ones and fetching new ones as needed to maintain capacity.
        """
        now = datetime.now()
        valid_proxies = [
            p for p in self._proxies
            if p not in self._blacklist and
            (p.deadline is None or now - p.deadline >= timedelta(seconds=10))
        ]
        new_proxies = self.fetch_proxies(max(self._capacity - len(valid_proxies), 0))
        self._proxies = deque(valid_proxies + new_proxies)
        self._blacklist.clear()

    def get_proxy(self) -> Proxy:
        """
        Get a valid Proxy from the collector. Invalid or expired proxies are skipped.
        :return: A Proxy object or None if no valid proxy is available
        """
        while len(self._proxies) > 0:
            p = self._proxies.popleft()
            if p.deadline and p.deadline <= datetime.now():
                continue
            if p in self._blacklist:
                continue
            self._proxies.append(p)
            return p
        return None

    def blacklist_proxy(self, proxy: Proxy) -> None:
        """
        Add a given Proxy to the blacklist.
        :param proxy: The Proxy to add to the blacklist
        """
        self._blacklist.add(proxy)

    def clear_blacklist(self) -> None:
        """
        Clear all Proxies from the blacklist.
        """
        self._blacklist.clear()