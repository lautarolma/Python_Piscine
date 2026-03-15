

class Plant():
    """Represent a plant with grow and aging capabilities.

    Atributes:
        name (str); The species or common name of the plant.
        height (int): Current height in centimeters.
        age (int): Internal age in days.
    """

    def __init__(self, plant_name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a Plant instance with name, height and age atributes.
        Height and age atributes are protected performing flexible user API and also
        protecting memory integrity in case of a invalid values involved in,
        """
        self.name = plant_name
        self.__height = 0
        self.__age = 0

        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """Returns the height in centimeters of an instance of a class Plant"""
        return self.__height

    def set_height(self, value) -> None:
        if value < 0:
            """Invalid imput. Height can not be negative"""            
        else:
            self.__height = value

    def get_age (self) -> int:
        """"Returns the Plant instance height in centimeters"""
        return self.__age

    def set_age (self, value) -> None:
        if value < 0:
            """Invalid imput. Age can not be negative"""            
        else:
            self.__age = value


class Flower(Plant):
    """
	Subclas of Plant class with special atribut: "color",
    and an special method: blooming.
    """

    def __init__(
                self, name: str, height: int, age: int, 
                color: str = "N/A"
                ) -> None:
        """
        """
        super().__init__(name, height, age)
        self.__color = "N/A"
        self.set_color(color)

    def __str__(self) -> str:
        return (
                    f"{self.name} (Flower): {self.get_height()}cm, {self.get_age()}"
                    f" days, {self.get_color()} color)"
                )

    def get_color(self) -> str:
        """Safe acces to Flower.color atribute."""
        return self.__color

    def set_color(self, color: str) -> None:
        """
        Validates and assigne the color value.

        Invalid Values:
        - Not a string type value.
        - Empty string value. For example "      ".
        """
        if isinstance(color, str) and color.strip():
            self.__color = color
        else:
            print(f"Invalid operation attempted: color '{color}' [REJECTED]")
            print("Security: Colr must be a non-empty string")

    def Bloom(self) -> None:
        """
        Emulate a blooming action.

        Gets a name from father constructor.
        """
        print(f"{self.get_name} is blooming beautifully! ")


if	__name__ == "__main__":
    rose = Flower("Rose", 24, 12, "white")
    print(rose)
