from rover import *

# (0,0).-------------> positive X
#     |
#     |
#     |
#     |
#     v
#     positive Y


#     N
#   W   E
#     S
#
def test_returns_initial_position_when_no_commands_given():
    assert rove((1, 1), "N", "") == (1, 1)
    assert rove((2, 2), "N", "") == (2, 2)


def test_returns_y_incremented_by_one_given_this_coordinate():
    assert rove((2, 2), "N", "f") == (2, 1)


def test_returns_y_decremented_by_one_given_this_coordinate():
    assert rove((2, 2), "N", "b") == (2, 3)


def test_returns_y_incremented_by_one_given_this_coordinate_xxxxxxxx():
    assert rove((2, 2), "W", "f") == (1, 2)


# def test_returns_x_decremented_by_one_when_turning_left_and_going_forwards():
#    assert rove((2, 2), "N", "lf") == (1, 2)
