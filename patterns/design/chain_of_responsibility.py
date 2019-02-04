"""
> Design pattern

Chain of Responsibility
=======================

26.11.2018
"""


def no_minus_number(content):
    return [x for x in content if x >= 0]


def no_zero(content):
    return [x for x in content if x > 0]


class ContentFilter:

    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content


filter = ContentFilter([
    no_minus_number,
    no_zero
])

filtered_content = filter.filter([1, 7, -1, 1, 0, 55, -9, 7])
print(filtered_content)
