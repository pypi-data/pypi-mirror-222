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


class CookiesProvider(object):
    """ CookiesProvider class"""

    def __init__(self):
        """
        Init interface
        """

        self._cookies = None

    @property
    def _is_cookie_fetched(self):
        """
        Check if cookies have been fetched from response
        :return: bool
        """

        return False if None is self._cookies else True

    def _fetch_cookies(self, headers):
        """
        Fetch cookies from response
        :param dict headers:  header
        :return: None
        """

        if 'set-cookie' in headers:
            self._cookies = headers.get('set-cookie')

    def _push_cookies(self):
        """
        Push cookies to request
        :return: str cookies
        """

        return self._cookies.strip()
