"""Main execution module"""

import sys

from interfaces import interfaces, parsers

from .settings import VALIDATOR
from .runner import TaskRunner

validator = VALIDATOR()

def main(arg):

    if len(arg) == 1 or arg[1] == 'console':
        parser = parsers.SimpleParser()
        interface = interfaces.ConsoleInterface(parser=parser)
    else:
        return

    taskrunner = TaskRunner(interface=interface, validator=validator)
    taskrunner.setup('Hello! ')
    taskrunner.run()


if __name__ == '__main__':
    main(sys.argv)
