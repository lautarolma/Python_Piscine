"""
This is a Garden Data Organizer wich can track multiple plants information.
"""


class Plant:
    """Plants in a garden system."""

    def __init__(self, plant_name: str, height: int, age: int) -> None:
        """Definicion of instances atributes of a Plant class."""
        self.name = plant_name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """Data manager of a garden system of several plants"""
    garden: list[Plant] = []
    garden.append(Plant("Rose", 25, 30))
    garden.append(Plant("Sunflower", 80, 45))
    garden.append(Plant("Cactus", 15, 120))

    print("=== Garden Plant Registry ===")
    for p in garden:
        print(f"{p.name}: {p.height}cm, {p.age} days old")


if __name__ == "__main__":
    ft_garden_data()
