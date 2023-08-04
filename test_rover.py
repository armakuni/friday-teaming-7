from rover import *


def test_can_call_empty_function():
    assert rove((1, 1), "N", "") == (1, 1)


def test_can_call_empty_function_1():
    assert rove((2, 2), "N", "") == (2, 2)
