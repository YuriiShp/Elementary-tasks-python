"""Module contains used classes

classes:
TNumber -- main class
NumEn -- english number class
NumUa -- ukrainian number class
"""


class TNumber:
    """Text representation of a number"""

    def __init__(self, val: int):
        """
        Keyword arguments:
        val -- integer value (max=999 999 999)
        """

        self.value = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: int):
        self._value = val

    def as_text(self, lang='eng'):
        """Return text representation of a number"""

        if lang == 'eng':
            return NumEng(self._value)

        if lang == 'ukr':
            return NumUa(self._value)

    @classmethod
    def from_console(cls, line):
        arg = line.strip()

        if arg.isdigit():
            arg = int(arg)
        return cls(arg)


class NumEng:
    """English number"""

    ZERO = 'zero'
    ONES = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    TEENS = {
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    TENS = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'fourty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }
    HUNDRED = 'hundred'
    THOUSAND = 'thousand'
    MILLION = 'million'

    HYPHEN = '-'
    SPACE = ' '

    def __init__(self, val: int):
        """
        Keyword arguments:
        val -- integer value (max=999 999 999)
        """

        self._value = val

    @property
    def written(self) -> str:
        """Return written representation of a number"""

        str_num = str(self._value)
        len_num = len(str_num)

        result = ''

        skip = False
        for i, v in enumerate(str_num):
            level = len_num - i

            if level == 1:
                # ONES
                if not skip:
                    if len_num == 1 and v == '0':
                        result = self.ZERO
                    else:
                        result += self.ONES[v]
                else:
                    skip = False

            if level == 2 or level == 5 or level == 8:
                # TENS
                if v == '0':
                    continue
                if v == '1':
                    result += self.TEENS[v + str_num[i + 1]] + self.SPACE
                    skip = True
                else:
                    if str_num[i + 1] != '0':
                        result += self.TENS[v] + self.HYPHEN
                    else:
                        result += self.TENS[v] + self.SPACE

            if level == 3 or level == 6 or level == 9:
                # HUNDREDS
                if v == '0':
                    continue
                result += self.ONES[v] + self.SPACE + \
                    self.HUNDRED + self.SPACE

            if level == 4:
                # THOUSAND
                if str_num[i - 2:i + 1] == '000':
                    continue
                if not skip:
                    result += self.ONES[v] + self.SPACE + \
                        self.THOUSAND + self.SPACE
                else:
                    result += self.THOUSAND + self.SPACE
                    skip = False

            if level == 7:
                # MILLION
                if str_num[i - 2:i + 1] == '000':
                    continue
                if not skip:
                    result += self.ONES[v] + self.SPACE + \
                        self.MILLION + self.SPACE
                else:
                    result += self.MILLION + self.SPACE
                    skip = False

        result = result.strip()

        return result

    def __str__(self):
        return self.written


class NumUa:
    """Ukrainian number"""

    ZERO = 'нуль'
    ONES = {
        '0': '',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'чотири',
        '5': 'п\'ять',
        '6': 'шість',
        '7': 'сім',
        '8': 'вісім',
        '9': 'дев\'ять'
    }
    ONES_F = {
        '1': 'одна',
        '2': 'дві',
    }
    TEENS = {
        '10': 'десять',
        '11': 'одинадцять',
        '12': 'дванадцять',
        '13': 'тринадцять',
        '14': 'чотирнадцять',
        '15': 'п\'ятнадцять',
        '16': 'шістнадцять',
        '17': 'сімнадцять',
        '18': 'вісімнадцять',
        '19': 'дев\'ятнадцять'
    }
    TENS = {
        '2': 'двадцять',
        '3': 'тридцять',
        '4': 'сорок',
        '5': 'п\'ятдесят',
        '6': 'шістдесят',
        '7': 'сімдесят',
        '8': 'вісімдесят',
        '9': 'дев\'яносто'
    }
    HUNDREDS = {
        '1': 'сто',
        '2': 'двісті',
        '3': 'триста',
        '4': 'чотириста',
        '5': 'п\'ятсот',
        '6': 'шістсот',
        '7': 'сімсот',
        '8': 'вісімсот',
        '9': 'дев\'ятсот'
    }
    THOUSAND = {
        'singular': 'тисяча',
        'plural_1': 'тисячі',
        'plural_2': 'тисяч'
    }
    MILLION = {
        'singular': 'мільйон',
        'plural_1': 'мільйони',
        'plural_2': 'мільйонів'
    }

    SPACE = ' '

    def __init__(self, val: int):
        """
        Keyword arguments:
        val -- integer value (max=999 999 999)
        """

        self._value = val

    @property
    def written(self) -> str:
        """Return written representation of a number"""

        str_num = str(self._value)
        len_num = len(str_num)

        result = ''

        skip = False
        for i, v in enumerate(str_num):
            level = len_num - i

            if level == 1:
                # ONES
                if not skip:
                    if len_num == 1 and v == '0':
                        result = self.ZERO
                    else:
                        result += self.ONES[v]
                else:
                    skip = False

            if level == 2 or level == 5 or level == 8:
                # TENS
                if v == '0':
                    continue
                if v == '1':
                    result += self.TEENS[v + str_num[i + 1]] + self.SPACE
                    skip = True
                else:
                    result += self.TENS[v] + self.SPACE

            if level == 3 or level == 6 or level == 9:
                # HUNDREDS
                if v == '0':
                    continue
                result += self.HUNDREDS[v] + self.SPACE

            if level == 4:
                # THOUSAND
                if str_num[i - 2:i + 1] == '000':
                    continue
                if not skip:
                    if v == '1':
                        result += self.ONES_F[v] + self.SPACE + \
                            self.THOUSAND['singular'] + self.SPACE
                    elif v == '2':
                        result += self.ONES_F[v] + self.SPACE + \
                            self.THOUSAND['plural_1'] + self.SPACE
                    elif v == '3' or v == '4':
                        result += self.ONES[v] + self.SPACE + \
                            self.THOUSAND['plural_1'] + self.SPACE
                    else:
                        result += self.ONES[v] + self.SPACE + \
                            self.THOUSAND['plural_2'] + self.SPACE

                else:
                    result += self.THOUSAND['plural_2'] + self.SPACE
                    skip = False

            if level == 7:
                # MILLION
                if str_num[i - 2:i + 1] == '000':
                    continue
                if not skip:
                    if v == '1':
                        result += self.ONES[v] + self.SPACE + \
                            self.MILLION['singular'] + self.SPACE
                    elif v == '2' or v == '3' or v == '4':
                        result += self.ONES[v] + self.SPACE + \
                            self.MILLION['plural_1'] + self.SPACE
                    else:
                        result += self.ONES[v] + self.SPACE + \
                            self.MILLION['plural_2'] + self.SPACE

                else:
                    result += self.MILLION['plural_2'] + self.SPACE
                    skip = False

        result = result.strip()

        return result

    def __str__(self):
        return self.written
