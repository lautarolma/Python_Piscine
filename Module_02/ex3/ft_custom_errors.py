"""
Custom garden-related exceptions and simple checks for demo purposes.

This module defines a small hierarchy of garden exceptions and helper
functions that raise those exceptions under certain conditions so the
behaviour can be demonstrated when running the module as a script.
"""


class GardenError(Exception):
    """Base exception for all garden-related errors."""
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised when a plant's health is below an acceptable threshold."""
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Raised when water level is insufficient for watering plants."""
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_health(plant_name: str = "tomato", health_level: int = 0) -> None:
    """
    Evaluate plant health (0-100).

    If `health_level` is below 50 the plant is considered wilting and a
    PlantError is raised.
    """
    if health_level < 50:
        raise PlantError(f"The {plant_name} plant is wilting!")


def test_water(water_level: int = 0) -> None:
    """
    Evaluate tank water level (0-100).

    If `water_level` is below 15 a WaterError is raised to indicate there
    is not enough water to water plants.
    """
    if water_level < 15:
        raise WaterError("Not enough water in the tank!")


def plant_checks() -> None:
    """
    Battery of tests that raise custom errors in different situations.

    Demonstrates catching specific custom exceptions and the base class
    GardenError which groups related errors.
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
