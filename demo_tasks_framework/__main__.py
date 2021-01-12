"""Main execution module"""

import sys

from interfaces import interfaces, parsers
from .dispatcher import Dispatcher

TASKS = {
    '5': {
        'title': 'Written numbers',
        'package': 'task_05_numbers'
    },
    '9': {
        'title': 'Palindromes',
        'package': 'task_09_palindromes'
    }
}


def main(arg):

    if len(arg) == 1 or arg[1] == 'console':
        parser = parsers.SimpleParser()
        interface = interfaces.ConsoleInterface(parser=parser)
    else:
        return

    controller = Dispatcher(interface=interface, tasks=TASKS)
    controller.setup()
    controller.run()


if __name__ == '__main__':

    main(sys.argv)
