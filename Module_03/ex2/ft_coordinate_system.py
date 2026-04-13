import math


def get_player_pos() -> tuple[float, float, float]:
    """
    Asks the user for the new player coordinates in the format x,y,z
    • Handles improper inputs
    • Retries until a valid set of coordinates is provided
    • Returns a tuple containing the player's current 3D coordinates
    """
    while True:
        input_user = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            parts = input_user.split(',')
            if len(parts) != 3:
                raise ValueError("Invalid syntax")

            coords = []
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
    p2: tuple[float, float, float] = (0, 0, 0)
) -> float:
    """
    Calculate Euclidean distance between two 3D points.
    If p2 is not provided, calculates distance to origin (0, 0, 0).
    """
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main() -> None:
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
