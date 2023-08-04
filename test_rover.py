from rover import *


def test_returns_initial_position_when_no_commands_given():
    assert rove((1, 1), "N", "") == (1, 1)
    assert rove((2, 2), "N", "") == (2, 2)
