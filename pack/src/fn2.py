from .fn1 import add


def sub(a, b):
    return a - b


def add_sub(a, b):
    return add(a, b) + sub(a, b)
