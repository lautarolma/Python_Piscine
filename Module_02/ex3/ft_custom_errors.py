class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_health(plant_name: str = "tomato", health_level: int = 0) -> None:
    """
    Evaluates plant helth (0-100)
    Above 50% plant begins to wither.
    """
    if health_level < 50:
        raise PlantError(f"The {plant_name} plant is wilting!")


def test_water(water_level: int = 0) -> None:
    """
    Evaluates tank water levels (0-100)
    Above 15% it's not enough water to watering plants.
    """
    if water_level < 15:
        raise WaterError("Not enough water in the tank!")


def plant_checks() -> None:
    """
    Batery of tests to raise costumized errors in diferent situations

    Intentional case of raising a generic error that encompasses
    particular cases.
    """
    print("Testing PlantError...")
    try:
        test_health("tomato", 40)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        test_water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        test_health("tomato", 20)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water(12)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    plant_checks()
    print()
    print("All custom error types work correctly!")
