from rover import *


def test_returns_initial_position_when_no_commands_given():
    assert rove((1, 1), "N", "") == (1, 1)
    assert rove((2, 2), "N", "") == (2, 2)


def test_returns_y_incremented_by_one_given_this_coordinate():
    assert rove((2, 2), "N", "f") == (2, 1)


def test_returns_y_decremented_by_one_given_this_coordinate():
    assert rove((2, 2), "N", "b") == (2, 3)
