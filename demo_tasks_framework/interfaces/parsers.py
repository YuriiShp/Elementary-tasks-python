"""Module contains text parsers"""

import re
from typing import List


INT = r'^(-)?(\d)+'
FLOAT = r'^(-)?(\d)*\.(\d)*'


class SimpleParser:
    """
    Parser class

    Parse console input, identifying objects of the following types:
    -- int
    -- float
    -- str
    """

    def __init__(self, re_int=INT, re_float=FLOAT):
        """
        Keyvalue arguments:
        re_int -- regular expression, representing <int>
        re_float -- regular expression, representing <float>
        """

        self.re_int = re_int
        self.re_float = re_float

    @property
    def re_int(self):
        return self.__re_int

    @re_int.setter
    def re_int(self, val: str):
        self.__re_int = re.compile(val)

    @property
    def re_float(self):
        return self.__re_float

    @re_float.setter
    def re_float(self, val: str):
        self.__re_float = re.compile(val)

    def parse(self, data: str) -> List:

        raw_list = data.split()

        result = []

        for element in raw_list:
            if self.__re_float.fullmatch(element):
                result.append(float(element))
            elif self.__re_int.fullmatch(element):
                result.append(int(element))
            else:
                result.append(element)

        return result
