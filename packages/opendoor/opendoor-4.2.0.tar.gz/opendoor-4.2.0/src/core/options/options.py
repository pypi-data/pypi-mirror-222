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

import sys
# noinspection PyCompatibility
from argparse import RawDescriptionHelpFormatter, OPTIONAL
from .exceptions import ArgumentParserError, ThrowingArgumentParser, OptionsError, FilterError
from .filter import Filter


class Options(object):

    """Options class"""

    def __init__(self):
        """
        Constructor
        :raise OptionsError
        """

        self.__standalone = ['version', 'update', 'examples', 'docs']
        self.__wizard_conf = 'opendoor.conf'

        __groups = {
            'request': "Request tools",
            'stream': "Stream tools",
            'debug': "Debug tools",
            'wordlist': "Wordlist tools",
            'sniff': "Sniff tools",
            'report': "Reports tools",
            'app': "Application tools"
        }

        __arguments = [
            {
                "group": "request",
                "args": "-p",
                "argl": "--port",
                "default": 80,
                "action": "store",
                "help": "Custom port (Default 80)",
                "type": int
            },
            {
                "group": "request",
                "args": "-m",
                "argl": "--method",
                "default": "HEAD",
                "action": "store",
                "help": "Request method (use HEAD as default)",
                "type": str
            },
            {
                "group": "stream",
                "args": "-t",
                "argl": "--threads",
                "default": 1,
                "action": "store",
                "help": "Allowed threads",
                "type": int
            },
            {
                "group": "request",
                "args": "-d",
                "argl": "--delay",
                "default": 0,
                "action": "store",
                "help": "Delay between requests threading",
                "type": float
            },
            {
                "group": "request",
                "args": None,
                "argl": "--timeout",
                "default": 30,
                "action": "store",
                "help": "Request timeout (30 sec default)",
                "type": int
            },
            {
                "group": "request",
                "args": "-r",
                "argl": "--retries",
                "default": 3,
                "action": "store",
                "help": "Max retries to reconnect (default 3)",
                "type": int
            },
            {
                "group": "request",
                "args": None,
                "argl": "--keep-alive",
                "default": False,
                "action": "store_true",
                "help": "Use keep-alive connection",
                "type": bool
            },
            {
                "group": "request",
                "args": None,
                "argl": "--accept-cookies",
                "default": False,
                "action": "store_true",
                "help": "Accept and route cookies from responses",
                "type": bool
            },
            {
                "group": "debug",
                "args": None,
                "argl": "--debug",
                "default": 0,
                "action": "store",
                "help": "Debug level -1 (silent), 1 - 3",
                "type": int
            },
            {
                "group": "request",
                "args": None,
                "argl": "--tor",
                "default": False,
                "action": "store_true",
                "help": "Using built-in proxylist",
                "type": bool
            },
            {
                "group": "request",
                "args": None,
                "argl": "--torlist",
                "default": None,
                "action": "store",
                "help": "Path to custom proxylist",
                "type": str
            },
            {
                "group": "request",
                "args": None,
                "argl": "--proxy",
                "default": None,
                "action": "store",
                "help": "Custom permanent proxy server",
                "type": str
            },
            {
                "group": "wordlist",
                "args": "-s",
                "argl": "--scan",
                "default": "directories",
                "action": "store",
                "help": "Scan type scan=directories or scan=subdomains",
                "type": str
            },
            {
                "group": "wordlist",
                "args": "-w",
                "argl": "--wordlist",
                "default": None,
                "action": "store",
                "help": "Path to custom wordlist",
                "type": str
            },
            {
                "group": "report",
                "args": None,
                "argl": "--reports",
                "default": "std",
                "action": "store",
                "help": "Scan reports (json,std,txt,html)",
                "type": str
            },
            {
                "group": "report",
                "args": None,
                "argl": "--reports-dir",
                "default": None,
                "action": "store",
                "help": "Path to custom reports dir",
                "nargs": 1,
                "type": str
            },
            {
                "group": "request",
                "args": None,
                "argl": "--random-agent",
                "default": False,
                "action": "store_true",
                "help": "Randomize user-agent per request",
                "type": bool
            },
            {
                "group": "wordlist",
                "args": None,
                "argl": "--random-list",
                "default": False,
                "action": "store_true",
                "help": "Shuffle scan list",
                "type": bool
            },
            {
                "group": "wordlist",
                "args": None,
                "argl": "--prefix",
                "default": None,
                "action": "store",
                "help": "Append path prefix to scan host",
                "type": str
            },
            {
                "group": "wordlist",
                "args": "-e",
                "argl": "--extensions",
                "default": None,
                "action": "store",
                "help": "Force use selected extensions for scan session -e php,json e.g",
                "type": str
            },
            {
                "group": "wordlist",
                "args": "-i",
                "argl": "--ignore-extensions",
                "default": None,
                "action": "store",
                "help": "Force ignore extensions for scan session -i aspx,jsp e.g",
                "type": str
            },
            {
                "group": "sniff",
                "args": None,
                "argl": "--sniff",
                "default": None,
                "action": "store",
                "help": "Response sniff plugins (indexof,collation,file,skipempty)",
                "type": str
            },
            {
                "group": "app",
                "args": None,
                "argl": "--update",
                "default": False,
                "action": "store_true",
                "help": "Update from CVS",
                "type": bool
            },
            {
                "group": "app",
                "args": None,
                "argl": "--version",
                "default": False,
                "action": "store_true",
                "help": "Get current version",
                "type": bool
            },
            {
                "group": "app",
                "args": None,
                "argl": "--examples",
                "default": False,
                "action": "store_true",
                "help": "Examples of usage",
                "type": bool
            },
            {
                "group": "app",
                "args": None,
                "argl": "--docs",
                "default": False,
                "action": "store_true",
                "help": "Read documentation",
                "type": bool
            },
            {
                "group": "app",
                "args": None,
                "argl": "--wizard",
                "default": None,
                "action": "store",
                "help": "Run wizard scanner from your config",
                "nargs": OPTIONAL,
                "const": self.__wizard_conf,
                "type": str
            }
        ]

        groupped = {}
        try:
            self.parser = ThrowingArgumentParser(formatter_class=RawDescriptionHelpFormatter)
            required_named = self.parser.add_argument_group('required named options')
            required_named.add_argument('--host', help="Target host (ip); --host http://example.com")
            arguments_len = len(__arguments)

            for group, description in sorted(__groups.items()):
                groupped[group] = self.parser.add_argument_group(description)

            for i in range(arguments_len):
                arg = __arguments[i]

                if 'nargs' in arg and arg['nargs'] == '?':
                    const = arg['const']
                else:
                    const = None

                if arg['args'] is None:
                    if bool == arg['type']:
                        groupped[arg['group']].add_argument(arg['argl'],
                                                            default=arg['default'],
                                                            action=arg['action'],
                                                            help=arg['help'])
                    elif None is not const:
                        groupped[arg['group']].add_argument(arg['argl'],
                                                            default=arg['default'],
                                                            action=arg['action'],
                                                            help=arg['help'],
                                                            nargs=arg['nargs'],
                                                            const=const,
                                                            type=arg['type'])
                    else:
                        groupped[arg['group']].add_argument(arg['argl'],
                                                            default=arg['default'],
                                                            action=arg['action'],
                                                            help=arg['help'],
                                                            type=arg['type'])
                else:
                    if bool == arg['type']:
                        groupped[arg['group']].add_argument(arg['args'],
                                                            arg['argl'],
                                                            default=arg['default'],
                                                            action=arg['action'],
                                                            help=arg['help'])
                    elif None is not const:
                        groupped[arg['group']].add_argument(arg['args'],
                                                            arg['argl'],
                                                            default=arg['default'],
                                                            action=arg['action'],
                                                            help=arg['help'],
                                                            nargs=arg['nargs'],
                                                            const=const,
                                                            type=arg['type'])
                    else:
                        groupped[arg['group']].add_argument(arg['args'],
                                                            arg['argl'],
                                                            default=arg['default'],
                                                            action=arg['action'],
                                                            help=arg['help'],
                                                            type=arg['type'])

            self.args = self.parser.parse_args()
        except (ArgumentParserError, KeyError) as error:
            raise OptionsError(error)

    def get_arg_values(self):
        """
        Get used input options
        :raise OptionsError
        :return: dict
        """

        args = {}

        try:
            arguments = self.args

            if not self.args.host \
                    and True is not self.args.version \
                    and True is not self.args.update \
                    and True is not self.args.docs \
                    and True is not self.args.examples \
                    and None is self.args.wizard:
                sys.exit(self.parser.print_help())

            if True is self.args.version or True is self.args.update \
                    or True is self.args.examples or True is self.args.docs:
                for arg, value in vars(arguments).items():
                    if arg in self.__standalone and True is value:
                        args[arg] = value
                        break
            else:

                for arg, value in vars(self.args).items():

                    if value:
                        args[arg] = value
                args = Filter.filter(args)

            return args

        except (AttributeError, FilterError, ArgumentParserError) as error:
            raise OptionsError(error)
