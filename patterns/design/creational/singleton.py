"""
> Creational patterns

Singleton
=========

По-русски - Одиночка. Используется, если нужны гарантии, что существует единственный экземпляр класса.
"""


class Logger:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger

