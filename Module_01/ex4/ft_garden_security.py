"""
Garden Security System Module.

Provides a Plant class that implements encapsulation to protect object
consistency. It validates data before storage, ensuring strict control over
how plant attributes are modified and accessed. The system intercepts invalid
or negative inputs and reports them through specific error messages.
"""


class Plant:
    """Represents a plant with protected attributes."""

    def __init__(
            self,
            plant_name: str,
            height: float = 0,
            age: int = 0) -> None:
        """
        Initializes a Plant instance with name, height and age
        attributes.

        Attributes are protected to provide a flexible user API while ensuring
        internal state integrity, even when invalid values are provided.
        """
        self._name = plant_name
        self._height = 0.0
        self._age = 0

        self.init_height(height)
        self.init_age(age)

    def show(self) -> None:
        """Display current plant state in the required format."""
        print(f"{self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")

    def get_age(self) -> int:
        """Safe reading access to age"""
        return self._age

    def set_age(self, value: int) -> None:
        """Validate modification of age"""
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")

    def init_age(self, value: int) -> None:
        """Initialize age with default fallback when value is invalid."""
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            self._age = 0
        else:
            self._age = value

    def get_height(self) -> float:
        """Safe reading access to height"""
        return self._height

    def set_height(self, amount: float) -> None:
        """Validate modification of height"""
        if amount < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(amount)
            print(f"Height updated: {int(self._height)}cm")

    def init_height(self, amount: float) -> None:
        """Initialize height with default fallback when value is invalid."""
        if amount < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            self._height = 0.0
        else:
            self._height = float(amount)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-8)
    print()

    print("Current state:", end=" ")
    rose.show()
