"""Module contains task runner class"""

from abstract.classes import TemplateTaskRunner

from .classes import TNumber


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

            next_response = self._interface.request_data(
                verbose='Choose language (eng/ua): ', parse=False)

            lang = 'eng'
            if next_response.lower() in ('ua', 'ukr', 'ukrainian'):
                lang = 'ukr'

            return {
                'user_input': data,
                'language': lang
            }

    def _calc(self, data: dict):
        """Logic"""

        return TNumber(val=data['user_input']).as_text(lang=data['language'])

    def _output(self, result):
        """Reporting result"""

        self._interface.report(obj=result, verbose='Number: ')
