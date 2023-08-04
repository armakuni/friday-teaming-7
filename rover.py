from typing import Tuple


def rove(
    coordinate: Tuple[int, int], initial_direction: str, commands: str
) -> Tuple[int, int]:
    return move(coordinate, initial_direction, commands)


def move(
    coordinate: Tuple[int, int], initial_direction: str, commands: str
) -> Tuple[int, int]:
    x_change = 0
    y_change = 0

    initial_x, initial_y = coordinate

    if initial_direction == "N":
        y_change -= 1

    if initial_direction == "W":
        x_change -= 1

    if initial_direction == "E":
        x_change += 1

    if initial_direction == "S":
        y_change += 1

    if commands == "f":
        return (initial_x + x_change, initial_y + y_change)

    if commands == "b":
        return (initial_x - x_change, initial_y - y_change)

    return coordinate
