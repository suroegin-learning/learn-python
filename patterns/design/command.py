"""
> Design pattern

Command
=======

Данный шаблон используется, когда нужно разделить во времени подготовку операции и ее исполнение.

Все подготовительные шаги объединяются в одной команде. Это позволяет добавлять дополнительные функциональные
возможности в будущем.

Так можно реализовать отмену совершенного действия или его повтор.
"""

import os
import time


class RenameFileCommand:

    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)


class History:

    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()


history = History()
history.execute(RenameFileCommand('datas/test_file.txt', 'datas/file_for_tests.txt'))
time.sleep(3)
history.undo()
