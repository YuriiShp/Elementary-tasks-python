"""Module contains task runner class"""

from abstract.classes import TemplateTaskRunner

from .classes import Number


class TaskRunner(TemplateTaskRunner):

    def _input(self):
        """Input data recieving and validation"""

        while True:
            response = self._interface.request_data(
                verbose='Input any positive integer number: ')

            if not response:
                self._interface.message(text=help(__package__))
                continue

            is_valid, data, message = self._validator.validate(
                value=response)

            if not is_valid:
                self._interface.message(text=message)
                continue

            return {
                'user_input': data
            }

    def _calc(self, data: dict):
        """Logic"""

        return Number(data['user_input']).get_palindromes()

    def _output(self, result):
        """Reporting result"""

        self._interface.report(obj=result, verbose='Palindromes: ')
