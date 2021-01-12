"""Module contains interfaces"""

from abstract.classes import Interface
from typing import List, Union

ConsoleTypes = Union[str, int, float, List]


class ConsoleInterface(Interface):
    """
    Console interface class

    Inputs and outputs data through the console, requires parser
    """

    def __init__(self, parser):
        """
        Keyvalue arguments:
        parser -- instance of the SimpleParcer class
        """

        self.__parser = parser

    def request_data(self, verbose=None, parse=True) -> Union[str, List]:
        """Request input from the user and return parsed data"""

        raw_data = input(verbose)
        if parse is True:
            return self.__parser.parse(raw_data)
        else:
            return raw_data.strip()

    def report(self, obj: ConsoleTypes, verbose=None, nline=False):
        """Print result to the console"""

        head_line_end = '\n' if nline else ''
        print(verbose, end=head_line_end)

        if isinstance(obj, list):
            if obj:
                for index, value in enumerate(obj):
                    if index < len(obj) - 1:
                        print(value, end=', ')
                    else:
                        print(value)
            else:
                print(0)

        else:
            print(obj)

    def message(self, text=None):
        """Print message"""

        print(text)
