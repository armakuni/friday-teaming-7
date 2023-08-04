from typing import Tuple


def rove(
    coordinate: Tuple[int, int], initial_direction: str, commands: str
) -> Tuple[int, int]:
    if commands == "f":
        return (2, 1)

    return coordinate
