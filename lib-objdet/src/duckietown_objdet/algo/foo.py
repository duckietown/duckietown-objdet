__all__ = [
    'FoobarAlgo',
]


class FoobarAlgo(object):

    def __init__(self, param1):
        self.param1 = param1

    def doit(self, value):
        return 1.0 + value + self.param1
