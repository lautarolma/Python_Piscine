"""
This is a Garden Data Organizer wich can track multiple plants information.
"""


class Plant:
    """
    Represent a plant with growth and aging capabilities.

    Atributes:
        name (str): The species or common name of the plant.
        height (int); Current height in centimeters.
        _age (int): Internal age in days.
    """

    def __init__(self, plant_name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance."""
        self.name = plant_name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Display the information of a Plant instance."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_garden_data() -> None:
    """Data manager of a garden system of several plants"""
    garden: list[Plant] = []
    garden.append(Plant("Rose", 25, 30))
    garden.append(Plant("Sunflower", 80, 45))
    garden.append(Plant("Cactus", 15, 120))

    print("=== Garden Plant Registry ===")
    for p in garden:
        p.show()


if __name__ == "__main__":
    ft_garden_data()
