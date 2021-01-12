"""Module contains dispatcher class"""

import importlib

from validators.validators import MockValidator


class Dispatcher:
    """
    Dispatcher class

    Run tasks based on user's choice
    """

    def __init__(self, interface, tasks: dict):
        """
        Keyvalue arguments:
        interface -- instance of Interface class
        tasks -- dict of avaiable tasks
        """

        self._interface = interface
        self._tasks = tasks
        self._repeat = True

    def setup(self):
        """List tasks"""

        self._interface.message(text='Tasks')

        task_list = [
            f'{i}. {self._tasks[i]["title"]}' for i in sorted(self._tasks.keys())
        ]

        for task in task_list:
            self._interface.message(text=task)

    def run(self):
        """Main execution routine"""

        while self._repeat is True:
            identifier = self._input()
            self._execute(task_id=identifier)
            self._continue()

    def _input(self):
        """Input data recieving and validation"""

        while True:
            response = self._interface.request_data(
                verbose='Choose task: ', parse=False)

            if not response:
                self._interface.message(text=help(__package__))
                continue

            if response not in self._tasks.keys():
                self._interface.message(text='Wrong task identifier! ')
                continue

            return response

    def _execute(self, task_id: int):
        """Logic"""

        validator = self.get_validator(task_id)
        runner = self.get_runner(task_id)
        if not runner:
            return

        taskrunner = runner(interface=self._interface, validator=validator)
        taskrunner.run()

    def _continue(self):
        """Run again"""

        response = self._interface.request_data(
            verbose='Do you want to run another task?: ', parse=False)
        if response.lower() in ('y', 'yes'):
            self._repeat = True
        else:
            self._repeat = False

    def get_runner(self, task_id: int):
        """Get TemplateTaskRunner child class from package"""

        package = self._tasks[task_id]['package']

        try:
            module = importlib.import_module(
                name=f'tasks.{package}.runner')
        except ModuleNotFoundError as err:
            self._interface.message(text=err)
            return

        module_classes = list(
            filter(
                lambda x: x[0].isupper(), dir(module)
            )
        )
        try:
            subclasses = list(
                filter(
                    lambda x: issubclass(
                        getattr(module, x), module.TemplateTaskRunner
                    ) and x != 'TemplateTaskRunner',
                    module_classes
                )
            )
        except AttributeError as err:
            self._interface.message(text=err)
            return
        else:
            if len(subclasses) == 0:
                message = 'Task runner class is not defined'
                self._interface.message(text=message)
            elif len(subclasses) >= 2:
                message = 'Two or more task runner classes were defined'
                self._interface.message(text=message)
            else:
                task_run_class = subclasses[0]
                return getattr(module, task_run_class)

    def get_validator(self, task_id: int):
        """Get Validator class"""

        package = self._tasks[task_id]['package']

        try:
            module = importlib.import_module(
                name=f'tasks.{package}.settings')
        except ModuleNotFoundError as err:
            self._interface.message(text=err)
            return

        if 'VALIDATOR' in dir(module):
            return module.VALIDATOR()
        else:
            return MockValidator()
