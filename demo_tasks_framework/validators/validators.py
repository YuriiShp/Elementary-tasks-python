"""Module contains validators"""

from abstract.classes import Validator


class PositiveIntValidator(Validator):
    """Validate positive integer"""

    def validate(self, value):

        if isinstance(value, list):
            if len(value) > 1:
                return False, value, f'Value should be <int> type,' \
                    f' got: {type(value)}'
            else:
                value = value[0]

        if not isinstance(value, int):
            return False, value, f'Value should be <int> type,' \
                f' got: {type(value)}'
        if value < 0:
            return False, value, f'Value should be grater then 0,' \
                f' got: {value}'

        return True, value, 'Success'


class LimitedIntValidator(PositiveIntValidator):
    """Validate positive integer"""

    def validate(self, value):

        is_valid, value, message = super().validate(value)

        if is_valid and value >= 10**9:
            return False, value, 'Value should be less then' \
                f' 1 000 000 000, got: {value}'

        return is_valid, value, message


class MockValidator(Validator):
    """No validation"""

    def validate(self, value):
        return True, value, None
