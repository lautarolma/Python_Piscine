"""
Garden evolution simuator.

This module provides tools to track and simulate the growth and aging
process of several plant species in a controled environment.
"""


class Plant():
    """
    Represent a plant with growth and aging capabilities.

    Atributes:
        name (str): The species or common name of the plant.
        height (int); Current height in centimeters.
        _age (int): Internal age in days.
    """

    def __init__(self, plant_name: str, height: int, _age: int) -> None:
        """Initialize a new Plant instance."""
        self.name = plant_name
        self.height = height
        self._age = _age

    def age(self) -> None:
        """Increment the plant's internal age by one day."""
        self._age += 1

    def grow(self, amount: int = 1) -> None:
        """Increment the plant's height by the specified amount."""
        self.height += amount

    def get_info(self) -> str:
        """Return a formatted string with the current plant status."""
        return f"{self.name}: {self.height}cm, {self._age} days old"


def ft_plant_growth() -> None:
    """
    Simulate a weekly growth cycle for a collection of plants.

    Calculate the growth size and display state changes.
    """
    garden: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 15, 45),
        Plant("Jasmin", 50, 30)
    ]
    print("=== Day 1 ===")
    for p in garden:
        print(p.get_info())
    print("=== Day 7 ===")
    for p in garden:
        for i in range(7):
            p.grow()
            p.age()
        print(p.get_info())
        print(f"Grow this week: +{i + 1}cm")


if __name__ == "__main__":
    ft_plant_growth()
