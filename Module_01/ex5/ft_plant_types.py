"""Specialized plant types for a garden system (Exercise 5)."""


class Plant:
    """Base plant class with common data and behavior."""

    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        """Initialize a Plant with name, height and age."""
        self.name = name
        self._height = 0.0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        """Return current height in centimeters."""
        return self._height

    def set_height(self, value: float) -> None:
        """Set height with validation against negative values."""
        if value >= 0:
            self._height = float(value)

    def get_age(self) -> int:
        """Return current age in days."""
        return self._age

    def set_age(self, value: int) -> None:
        """Set age with validation against negative values."""
        if value >= 0:
            self._age = value

    def grow(self, amount: float = 1.0) -> None:
        """Increase plant height."""
        self._height += float(amount)

    def age(self, amount: int = 1) -> None:
        """Increase plant age."""
        self._age += amount

    def show(self) -> None:
        """Display basic plant information."""
        print(f"{self.name}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")


class Flower(Plant):
    """Specialized plant type for flowers."""

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        color: str = "unknown"
    ) -> None:
        """Initialize a Flower with color and bloom status."""
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Set flower as blooming."""
        self.is_blooming = True

    def show(self) -> None:
        """Display flower information with bloom status."""
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    """Specialized plant type for trees."""

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        trunk_diameter: float = 0.0
    ) -> None:
        """Initialize a Tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Display a message describing the tree shade."""
        print(
            f"Tree {self.name} now produces a shade of {self.get_height()}cm "
            f"long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        """Display tree information with trunk diameter."""
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    """Specialized plant type for vegetables."""

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        harvest_season: str = "unknown"
    ) -> None:
        """Initialize a Vegetable with harvest season and nutrition value."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float = 1.0) -> None:
        """Increase height and nutritional value."""
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, amount: int = 1) -> None:
        """Increase age and nutritional value."""
        super().age(amount)
        self.nutritional_value += 1

    def show(self) -> None:
        """Display vegetable information with extra attributes."""
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(10):
        tomato.grow(4.2)
        tomato.age(2)
    tomato.show()
