"""Module contains used classes (OOP part)"""

from typing import List


class Number:
    """Enables palindromes extraction"""

    def __init__(self, val: int):
        """
        Keyword arguments:
        val -- positive integer number
        """

        self.value = val

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, val: int):
        self._value = val

    def is_palindrome(self) -> bool:
        """Check if Number is a palindrome"""

        num = str(self._value)

        if len(num) == 1:
            return False

        while len(num) > 1:
            if num[0] != num[-1]:
                return False
            num = num[1:-1]

        return True

    def get_palindromes(self) -> List['Number']:
        """Extracts palindromes from Number"""

        num = str(self._value)
        palindromes = []

        while num:
            for i in range(len(num)):
                part = Number(int(num[i:]))
                if part.is_palindrome() and part not in palindromes:
                    palindromes.append(part)
            num = num[:-1]
        return palindromes

    def __eq__(self, other: 'Number'):
        return self.value == other.value

    def __repr__(self) -> str:
        return str(self._value)

    @classmethod
    def from_console(cls, line: str) -> 'Number':
        arg = line.strip()

        if arg.isdigit():
            arg = int(arg)
        return cls(arg)
