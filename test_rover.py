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
def test_no_movement():
    assert rove((1, 1), "N", "") == (1, 1)
    assert rove((2, 2), "N", "") == (2, 2)


def test_forwards():
    assert rove((2, 2), "N", "f") == (2, 1)
    assert rove((2, 2), "W", "f") == (1, 2)
    assert rove((2, 2), "E", "f") == (3, 2)
    assert rove((2, 2), "S", "f") == (2, 3)
    assert rove((2, 2), "S", "ff") == (2, 4)


def test_backwards():
    assert rove((2, 2), "N", "b") == (2, 3)
    assert rove((2, 2), "S", "bb") == (2, 0)


def test_turning_left():
    assert rove((1, 1), "N", "llrr") == (1, 1)
    assert rove((2, 2), "N", "lf") == (1, 2)
    assert rove((2, 2), "E", "lf") == (2, 1)
    assert rove((2, 2), "S", "lf") == (3, 2)
