class GardenError(Exception):
    """Base exception for all garden-related errors."""
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised when there is an issue with a plant."""
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """
    Validates if a plant can be watered based on its capitalization.
    - Succeeds if capitalized.
    - Raises PlantError if not capitalized.
    """
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants_list: tuple[str, ...]) -> None:
    """
    Simulates opening the watering system, watering all plants,
    handling uncapitalized plant errors by stopping immediately,
    and ALWAYS closing the system via a finally block.
    """
    print("Opening watering system")

    try:
        for plant in plants_list:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()

    print("Testing valid plants...")
    valid_group = ("Tomato", "Lettuce", "Carrots")
    test_watering_system(valid_group)
    print()

    print("Testing invalid plants...")
    invalid_group = ("Tomato", "lettuce", "Carrots")
    test_watering_system(invalid_group)
    print()

    print("Cleanup always happens, even with errors!")
