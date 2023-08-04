from rover import *


def test_can_call_empty_function():
    assert rove((1, 1), "N", "") == (1, 1)
