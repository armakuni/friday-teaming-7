from typing import Tuple


def rove(
    coordinate: Tuple[int, int], initial_direction: str, commands: str
) -> Tuple[int, int]:
    current_coordinate = coordinate
    current_direction = initial_direction

    for command in commands:
        if command == "l":
            current_direction = turn_left(current_direction)

        current_coordinate = move(current_coordinate, current_direction, command)

    return current_coordinate


def move(
    coordinate: Tuple[int, int], initial_direction: str, command: str
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

    if command == "f":
        return (initial_x + x_change, initial_y + y_change)

    if command == "b":
        return (initial_x - x_change, initial_y - y_change)

    return coordinate


def turn_left(current_direction: str) -> str:
    return {"N": "W", "S": "E", "E": "N", "W": "S"}[current_direction]
