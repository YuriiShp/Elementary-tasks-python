"""Module contains abstract classes"""

from abc import ABC, abstractmethod
from typing import Any


class TemplateTaskRunner(ABC):
    """Task run abstract base class"""

    def __init__(self, interface, validator):
        """
        Keyvalue arguments:
        interface -- instance of Interface class
        validator -- instance of Validator class
        """

        self._interface = interface
        self._validator = validator
        self._repeat = True

    def setup(self, greating: str):
        """Greetings"""

        self._interface.message(text=greating)

    def run(self):
        """Main execution routine"""

        while self._repeat is True:
            validated_data = self._input()
            result = self._calc(validated_data)
            self._output(result)
            self._continue()

    @abstractmethod
    def _input(self):
        pass

    @abstractmethod
    def _calc(self, data: dict):
        pass

    @abstractmethod
    def _output(self, result: Any):
        pass

    def _continue(self):
        """Run again"""

        response = self._interface.request_data(
            verbose='Do you want to continue?: ', parse=False)
        if response.lower() in ('y', 'yes'):
            self._repeat = True
        else:
            self._repeat = False


class Interface(ABC):
    """Abstract base interface class"""

    @abstractmethod
    def request_data(self):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def message(self):
        pass


class Validator(ABC):
    """Abstract base validator class"""

    @abstractmethod
    def validate(self, value):
        pass
