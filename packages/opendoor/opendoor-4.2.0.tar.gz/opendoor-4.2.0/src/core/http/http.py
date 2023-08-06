# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Brain Storm Team
"""

from urllib3 import HTTPConnectionPool, PoolManager, Timeout
from urllib3.exceptions import MaxRetryError, ReadTimeoutError, ConnectTimeoutError, HostChangedError
from src.core import helper
from .exceptions import HttpRequestError
from .providers import DebugProvider
from .providers import RequestProvider


class HttpRequest(RequestProvider, DebugProvider):

    """HttpRequest class"""

    def __init__(self, config, debug, **kwargs):
        """
        HttpRequest instance
        :param src.lib.browser.config.Config config: global configurations
        :param DebugProvider debug: debugger
        """

        try:
            self.__tpl = kwargs.get('tpl')
            RequestProvider.__init__(self, config, agent_list=kwargs.get('agent_list'))
            self.__headers = self._headers
            self.__connection_header = 'default'
            if True is config.keep_alive:
                self.__connection_header = self._keep_alive
        except (TypeError, ValueError) as error:
            raise HttpRequestError(error)

        self.__cfg = config
        self.__debug = debug

        if self.__cfg.DEFAULT_SCAN == self.__cfg.scan:
            self.__pool = self.__http_pool()

    def __http_pool(self):
        """
        Create HTTP connection pool
        :raise HttpRequestError
        :return: urllib3.HTTPConnectionPool
        """

        try:
            pool = HTTPConnectionPool(self.__cfg.host,
                                      port=self.__cfg.port,
                                      maxsize=self.__cfg.threads,
                                      timeout=Timeout(connect=self.__cfg.timeout, read=self.__cfg.timeout),
                                      block=True)
            if self._HTTP_DBG_LEVEL <= self.__debug.level:
                self.__debug.debug_connection_pool('http_pool_start', pool, self.__connection_header)
            return pool
        except Exception as error:
            raise HttpRequestError(str(error))

    def request(self, url):
        """
        Client request HTTP
        :param str url: request uri
        :return: urllib3.HTTPResponse
        """

        self.__headers.update({'User-Agent': self._user_agent})
        if 'default' is not self.__connection_header:
            self.__headers.update({'Connection': self.__connection_header})
        if self._HTTP_DBG_LEVEL <= self.__debug.level:
            self.__debug.debug_request(self.__headers, url, self.__cfg.method)
        try:
            if self.__cfg.DEFAULT_SCAN == self.__cfg.scan:
                response = self.__pool.request(self.__cfg.method,
                                               helper.parse_url(url).path,
                                               headers=self.__headers,
                                               retries=self.__cfg.retries,
                                               assert_same_host=True,
                                               redirect=False)
                self.cookies_middleware(is_accept=self.__cfg.accept_cookies, response=response)
            else:
                response = PoolManager().request(self.__cfg.method, url,
                                                 headers=self.__headers,
                                                 retries=self.__cfg.retries,
                                                 assert_same_host=False,
                                                 redirect=False,
                                                 timeout=Timeout(connect=self.__cfg.timeout, read=self.__cfg.timeout))
            return response

        except MaxRetryError:
            if self.__cfg.DEFAULT_SCAN == self.__cfg.scan:
                self.__tpl.warning(key='max_retry_error', url=helper.parse_url(url).path)
            pass

        except HostChangedError as error:
            self.__tpl.warning(key='host_changed_error', details=error)
            pass

        except ReadTimeoutError:
            self.__tpl.warning(key='read_timeout_error', url=url)
            pass

        except ConnectTimeoutError:
            self.__tpl.warning(key='connection_timeout_error', url=url)
            pass
