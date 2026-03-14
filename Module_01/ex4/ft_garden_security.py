"""
Garden Security System Module.

Provides a SecurePlant class that implements encapsulation to protect object
consistency. It validates data before storage, ensuring strict control over
how plant attributes are modified and accessed. The system intercepts invalid
or negative inputs and reports them through specific error messages.
"""


class SecurePlant():
    """Represents a plant with protected attributes via Name Mangling."""

    def __init__(self, plant_name: str, height: int = 0, age: int = 0) -> None:
        """
        Initializes a SecurePlant instance with name, height and age
        attributes.

        Attributes are protected to provide a flexible user API while ensuring
        internal state integrity, even when invalid values are provided.
        """
        self.__name = plant_name
        self.__height = 0
        self.__age = 0
#       The initialization before prevents atribute creation from invalid
#       inputs

        print(f"Plant created: {self.__name}")

        self.set_height(height)
        self.set_age(age)

    def __str__(self) -> str:
        """
        Special method to fetch the object in a string format.
        Its internally called by the action print(object).
        """
        return (
                    f"Current plant: {self.__name} ({self.__height}cm, "
                    f"{self.__age} days)"
                )

    def get_age(self) -> int:
        """Safe reading access to age"""
        return self.__age

    def set_age(self, value) -> None:
        """Validate modification of age"""
        if value < 0:
            print(
                    f"\nInvalid operation attempted: "
                    f"age {value} days [REJECTED]"
            )
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        """Safe reading access to height"""
        return self.__height

    def set_height(self, amount: int) -> None:
        """Validate modification of height"""
        if amount < 0:
            print(
                    f"\nInvalid operation attempted: "
                    f"height {amount}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = amount
            print(f"Height updated: {amount}cm [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print()
    print(rose)
