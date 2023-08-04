from typing import Tuple


def rove(
    coordinate: Tuple[int, int], initial_direction: str, commands: str
) -> Tuple[int, int]:
    current_coordinate = coordinate

    for command in commands:
        current_coordinate = move(current_coordinate, initial_direction, command)

    return current_coordinate


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
