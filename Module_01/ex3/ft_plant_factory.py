"""
Implementation of a Garden plant factory with simple and optimized
creation of various plants.
"""


class Plant():
    """
    Represent a plant with growth and aging capabilities.

    Atributes:
        name (str): The species or common name of the plant.
        height (int); Current height in centimeters.
        _age (int): Internal age in days.
    """

    def __init__(self, plant_name: str, height: float, _age: int) -> None:
        """Initialize a new Plant instance."""
        self.name = plant_name
        self.height = float(height)
        self._age = _age

    def age(self) -> None:
        """Increment the plant's internal age by one day."""
        self._age += 1

    def grow(self, amount: float = 1.0) -> None:
        """Increment the plant's height by the specified amount."""
        self.height += amount

    def show(self) -> None:
        """Display the information of a Plant instance."""
        print(f"Created: {self.name}: {self.height}cm, {self._age} days old")


def ft_plant_factory() -> None:
    """
    Streamline creation process for many plants, quickly, using Plant class
    with different starting values.
    """
    raw_data: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    garden: list[Plant] = []

    for name, height, age in raw_data:
        garden.append(Plant(name, height, age))

    print("=== Plant Factory Output ===")
    for p in garden:
        p.show()


if __name__ == "__main__":
    ft_plant_factory()
