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

from src.core import CoreSystemError, FileSystemError
from src.core import CoreConfig
from src.core import filesystem
from src.core import helper
from src.core import process
from src.core import sys
# noinspection PyPep8Naming
from src.lib.tpl import Tpl as tpl
from .exceptions import PackageError


class Package(object):
    """Package class"""

    remote_version = None

    @staticmethod
    def check_interpreter():
        """
        Get interpreter version
        :return: dict or bool
        """

        versions = CoreConfig.get('info').get('required_versions')
        actual_version = sys.version()
        target_compare = (actual_version == versions.get('minor') or actual_version == versions.get('major'))
        relative_compare = (helper.is_less(versions.get('minor'), actual_version) is True or
                            helper.is_more(actual_version, versions.get('major')) is True)

        if target_compare or relative_compare:
            return True
        else:
            return {
                'status': False,
                'actual': actual_version, 'expected': versions.get('minor') + ' -> ' + versions.get('major')
            }

    @staticmethod
    def examples():
        """
        Load examples of usage
        :return: str
        """

        examples = CoreConfig.get('examples')
        return examples

    @staticmethod
    def banner():
        """
        Load application banner

        :raise PackageError
        :return: str
        """

        try:

            banner = CoreConfig.get('banner').format(
                tpl.line('Directories: {0}'.format(Package.__directories_count()), color='blue'),
                tpl.line('Subdomains: {0}'.format(Package.__subdomains_count()), color='blue'),
                tpl.line('Browsers: {0}'.format(Package.__browsers_count()), color='blue'),
                tpl.line('Proxies: {0}'.format(Package.__proxies_count()), color='blue'),
                tpl.line(Package.__license(), color='blue'))

            return banner

        except (FileSystemError, CoreSystemError, PackageError) as error:
            raise PackageError(error)

    @staticmethod
    def version():
        """
        Load application version
        :raise PackageError
        :return: str
        """

        try:

            version = CoreConfig.get('version').format(Package.__app_name(), Package.__current_version(),
                                                       Package.__remote_version(), Package.__repo(),
                                                       Package.__license())
            return version

        except (FileSystemError, CoreSystemError, PackageError) as error:
            raise PackageError(error)

    @staticmethod
    def wizard(config):
        """
        Get application wizard (read from config)
        :param str config: configuration file
        :raise PackageError
        :return: str
        """

        try:
            config = filesystem.readcfg(config)
            # noinspection PyProtectedMember
            params = dict(config._sections['general'])

            for key, val in params.items():
                params[key] = None if val == 'None' else val
                if None is not params[key]:
                    if params[key].isdigit():
                        params[key] = int(float(params[key]))
                    elif params[key] in ['True', 'False']:
                        if params[key] == 'True':
                            params[key] = True
                        else:
                            params[key] = False
                    else:
                        params[key] = params[key].strip()
            return params

        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def docs():
        """
        Open documentation
        :raise PackageError
        :return: bool
        """
        docurl = CoreConfig.get('info').get('documentation')
        return helper.openbrowser(docurl)

    @staticmethod
    def update():
        """
        Check for update
        :raise PackageError
        :return: str
        """

        try:
            if False is sys().is_windows:
                status = process.execute(CoreConfig.get('command').get('cvsupdate'))
                upd_status = tpl.line(status, color='green')
                msg = CoreConfig.get('update').format(status=upd_status)
            else:
                msg = CoreConfig.get('update').format(status=tpl.line(key='upd_win_stat'))
            return msg
        except (AttributeError, CoreSystemError) as error:
            raise PackageError(error)

    @staticmethod
    def local_version():
        """
        Get application local version
        :raise PackageError
        :return: str
        """

        try:
            version = CoreConfig.get('info').get('version')
            return version
        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __app_name():
        """
        Get application name
        :raise PackageError
        :return: str
        """

        try:
            name = CoreConfig.get('info').get('name')
            return name
        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __remote_version():
        """
        Get application remote version
        :raise PackageError
        :return: str
        """

        if None is Package.remote_version:

            try:
                request_uri = CoreConfig.get('info').get('remote_version')
                result = process.execute('curl -sb GET {uri}'.format(uri=request_uri))
                Package.remote_version = str(result, "utf-8")
                return Package.remote_version

            except (FileSystemError, CoreSystemError) as error:
                raise PackageError(error)
        else:
            return Package.remote_version

    @staticmethod
    def __current_version():
        """
        Get current application version
        :raise PackageError
        :return: str
        """

        try:
            local = Package.local_version()
            remote = Package.__remote_version()
            if True is helper.is_less(local, remote):
                current_version = tpl.line(local, color='red')
            else:
                current_version = tpl.line(local, color='green')
            return current_version

        except (FileSystemError, CoreSystemError, PackageError) as error:
            raise PackageError(error)

    @staticmethod
    def __repo():
        """
        Get application repository url
        :raise PackageError
        :return: str
        """

        try:
            repository = CoreConfig.get('info').get('repository')
            return repository
        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __license():
        """
        Get application license
        :raise PackageError
        :return: str
        """

        try:
            license_info = CoreConfig.get('info').get('license')
            return license_info
        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __directories_count():
        """
        Get number of directories in basic wordlist
        :raise PackageError
        :return: int
        """

        try:
            filename = CoreConfig.get('data').get('directories')
            count = filesystem.count_lines(filename)

            return count

        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __subdomains_count():
        """
        Get the number of subdomains in basic wordlist
        :raise PackageError
        :return: int
        """

        try:
            filename = CoreConfig.get('data').get('subdomains')
            count = filesystem.count_lines(filename)

            return count

        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __browsers_count():
        """
        Get the number of browsers in basic wordlist
        :raise PackageError
        :return: int
        """

        try:
            filename = CoreConfig.get('data').get('useragents')
            count = filesystem.count_lines(filename)

            return count

        except FileSystemError as error:
            raise PackageError(str(error))

    @staticmethod
    def __proxies_count():
        """
        Get number of proxies in basic wordlist
        :raise PackageError
        :return: int
        """

        try:
            filename = CoreConfig.get('data').get('proxies')
            count = filesystem.count_lines(filename)

            return count

        except FileSystemError as error:
            raise PackageError(str(error))
