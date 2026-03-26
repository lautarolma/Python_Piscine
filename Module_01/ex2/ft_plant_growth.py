"""
Garden evolution simuator.

This module provides tools to track and simulate the growth and aging
process of several plant species in a controled environment.
"""


class Plant:
    """
    Represent a plant with growth and aging capabilities.

    Atributes:
        name (str): The species or common name of the plant.
        height (int); Current height in centimeters.
        _age (int): Internal age in days.
    """

    def __init__(
        self,
        plant_name: str,
        height: float,
        _age: int,
        growth_rate: float = 0.8
    ) -> None:
        """Initialize a new Plant instance."""
        self.name = plant_name
        self.height = height
        self._age = _age
        self.growth_rate = growth_rate

    def show(self) -> None:
        """Display the information of a Plant instance."""
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")

    def age(self) -> None:
        """Increment the plant's internal age by one day."""
        self._age += 1

    def grow(self) -> None:
        """Increment the plant's height using its own growth rate."""
        self.height += self.growth_rate

    def get_height(self) -> float:
        """Return current plant height in centimeters."""
        return self.height


def ft_plant_growth() -> None:
    """
    Simulate a weekly growth cycle for a collection of plants.

    Calculate the growth size and display state changes.
    """

    garden: list[Plant] = []
    garden.append(Plant("Rose", 24.2, 29))
    growth_days = 7

    print("=== Garden Plant Growth ===")
    for day in range(1, growth_days + 1):
        for plant in garden:
            plant.grow()
            plant.age()

        print(f"=== Day {day} ===")
        for plant in garden:
            plant.show()
    week_growth = round(garden[0].growth_rate * growth_days)
    print(f"Growth this week: {week_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
