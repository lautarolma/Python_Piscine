"""Game coordinate utilities for 3D player positions.

Provides a small interactive utility to read 3D coordinates from the
user, validate them, and compute Euclidean distances.
"""

import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompt the user until valid 3D coordinates 'x,y,z' are provided.

    Returns a tuple of three floats representing the player's position.
    Prints short, specific error messages for invalid input and retries
    until a valid triple is entered.
    """
    while True:
        prompt = input(
            "Enter new coordinates as floats in format "
            "'x,y,z': "
        )
        try:
            parts = prompt.split(',')
            if len(parts) != 3:
                raise ValueError("Invalid syntax")

            coords: list[float] = []
            for part in parts:
                value = float(part.strip())
                coords.append(value)

            return (coords[0], coords[1], coords[2])

        except ValueError as e:
            if str(e) == "Invalid syntax":
                print("Invalid syntax")
            else:
                for part in parts:
                    try:
                        float(part.strip())
                    except ValueError:
                        print(f"Error on parameter '{part.strip()}': {e}")
                        break


def calculate_distance(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float] = (0.0, 0.0, 0.0)
) -> float:
    """Return the Euclidean distance between two 3D points.

    If p2 is omitted, the distance to the origin is returned.
    """
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main() -> None:
    """Interactive main for reading two positions and printing distances."""
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_to_center = calculate_distance(pos1)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    distance = calculate_distance(pos2, pos1)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
