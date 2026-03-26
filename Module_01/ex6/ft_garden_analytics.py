"""Garden analytics module.

This module defines a simple garden analytics system with classes for
plants, flowers, trees, and seeds. It includes methods for tracking
growth, aging, blooming, and shade production, along with statistics
for method calls. The `main` function demonstrates the behavior of the
classes and their interactions.
"""


class Plant:
    """
    Base class that defines common plant data in a garden system.

    Attributes:
        name (str): Species or common name of the plant.
        height (float): Current height in centimeters.
        age (int): Internal age in days.
    """

    class Stats:
        """
        Internal call counters for `grow`, `age`, and `show` methods.

        Helper class tracking per-instance method-call stats.
        """

        def __init__(self) -> None:
            """Initialize call counters for tracked methods.

            Initializes counters for:
                - grow method calls
                - age method calls
                - show method calls
            """
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow_call(self) -> None:
            """Increment the grow method call counter by one."""
            self._grow_calls += 1

        def record_age_call(self) -> None:
            """Increment the age method call counter by one."""
            self._age_calls += 1

        def record_show_call(self) -> None:
            """Increment the show method call counter by one."""
            self._show_calls += 1

        def display(self) -> None:
            """Display method-call statistics for the current instance."""
            print(
                f"Stats: {self._grow_calls} grow, {self._age_calls}"
                f" age, {self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0
    ) -> None:
        """
        Initialize a Plant with name, height, and age.

        Height and age validated via setters for safety.
        """
        self.name = name
        self._height = float(0.0)
        self._age = 0

        self.set_height(height)
        self.set_age(age)
        self._stats = self.Stats()

    def get_height(self) -> float:
        """Return the plant height in centimeters."""
        return self._height

    def set_height(self, value: float) -> None:
        """Set the plant height if the value is non-negative."""
        if value < 0:
            print(f"Invalid input '{value}' [REJECTED]")
            print("Security: Height cannot be negative")
        else:
            self._height = float(value)

    def get_age(self) -> int:
        """Return the plant age in days."""
        return self._age

    def set_age(self, value: int) -> None:
        """Set the plant age if the value is non-negative."""
        if value < 0:
            print(f"Invalid input '{value}' [REJECTED]")
            print("Security: Age cannot be negative")
        else:
            self._age = value

    def age(self, amount: int = 1) -> None:
        """Increment the plant's age by the specified amount."""
        self._stats.record_age_call()
        self._age += amount

    def grow(self, amount: float = 1.0) -> None:
        """Increase the plant's height by the specified amount."""
        self._stats.record_grow_call()
        self._height += float(amount)

    def show(self) -> None:
        """Display a one-line summary of the plant's current state."""
        self._stats.record_show_call()
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def show_statistics(self) -> None:
        """Display method-call statistics for the current plant instance."""
        print(f"[statistics for {self.name}]")
        self._stats.display()

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        """Return True when the given number of days is greater than 365."""
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """Create and return a generic unnamed plant instance."""
        return cls("Unknown plant")


class Flower(Plant):
    """Plant specialization that tracks color and blooming state."""

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        color: str = "unknown",
        is_blooming: bool = False
    ) -> None:
        """Initialize a Flower with color and blooming state attributes."""
        super().__init__(name, height, age)
        self.is_blooming = is_blooming
        self._color = "unknown"
        self.set_color(color)

    def get_color(self) -> str:
        """Return the flower's color."""
        return self._color

    def set_color(self, value: object) -> None:
        """Set the flower's color if the input value is a valid string."""
        if isinstance(value, str):
            self._color = value
        else:
            print(f"Invalid input '{value}' [REJECTED]")
            print("Security: color must be a string")

    def bloom(self) -> None:
        """Mark the flower as currently blooming."""
        self.is_blooming = True

    def show(self) -> None:
        """Display flower's information (color and blooming info)."""
        super().show()
        print(f" Color: {self.get_color()}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    """Plant specialization that models trunk diameter and shade production."""

    class Stats(Plant.Stats):
        """
        Extend Plant._Stats with produce_shade call tracking.

        Customizes the statistics output to include shade production calls.
        """

        def __init__(self) -> None:
            """Initialize counters including produce_shade method calls."""
            super().__init__()
            self._shade_calls: int = 0

        def record_shade_call(self) -> None:
            """Increment the produce_shade method call counter by one."""
            self._shade_calls += 1

        def display(self) -> None:
            """
            Display method-call statistics for the current Tree instance.
            """
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        trunk_diameter: float = 0.0,
    ) -> None:
        """Initialize a Tree with trunk diameter tracking."""
        super().__init__(name, height, age)
        self._stats = self.Stats()
        self._trunk_diameter = 0.0

        self.set_trunk_diameter(trunk_diameter)

    def get_trunk_diameter(self) -> float:
        """Return the trunk diameter in centimeters."""
        return self._trunk_diameter

    def set_trunk_diameter(self, value: float) -> None:
        """Set the trunk diameter if the value is non-negative."""
        if value < 0:
            print(f"Invalid input '{value}' [REJECTED]")
            print("Security: trunk_diameter cannot be negative")
        else:
            self._trunk_diameter = float(value)

    def produce_shade(self) -> None:
        """Record and display the tree's current shade production details."""
        if isinstance(self._stats, self.Stats):
            self._stats.record_shade_call()
        print(
            f"Tree {self.name} now produces a shade of {self.get_height()}"
            f"cm long and {self.get_trunk_diameter()}cm wide."
        )

    def show(self) -> None:
        """Display the tree's information and trunk diameter."""
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diameter()}cm")


class Seed(Flower):
    """Flower specialization that tracks seed production."""

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        color: str = "unknown",
        is_blooming: bool = False,
        seed_count: int = 0,
    ) -> None:
        """Initialize a seed-bearing Flower with an initial seed count."""
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def get_seed_count(self) -> int:
        """Return the current number of seeds produced by the flower."""
        return self._seed_count

    def set_seed_count(self, amount: int) -> None:
        """Update the number of seeds for the instance."""
        if amount < 0:
            print(f"Invalid input '{amount}' [REJECTED]")
            print("Security: Seed count cannot be negative")
        else:
            self._seed_count = amount

    def show(self) -> None:
        """Display the flower's information and current seed count."""
        super().show()
        print(f" Seeds: {self.get_seed_count()}")


def display_plant_statistics(plant: Plant) -> None:
    """Display method-call statistics for any Plant instance."""
    plant.show_statistics()


def main() -> None:
    """Execute demonstration scenarios for the garden analytics system."""
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(
        f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    rose.show_statistics()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.show_statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_statistics()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.set_seed_count(42)
    sunflower.show()
    sunflower.show_statistics()

    print("\n=== Anonymous")
    unknown_plant = Plant.create_anonymous()
    unknown_plant.show()
    unknown_plant.show_statistics()


if __name__ == "__main__":
    main()
