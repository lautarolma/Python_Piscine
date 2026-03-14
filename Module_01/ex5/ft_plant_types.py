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
        self.__name = plant_name
        self.__height = 0
        self.__age = 0

        set_self.__height(height)
        set_self.__age(age)

    def get_height(self) -> int:
        """Returns the height in centimeters of an instance of a class Plant"""
        return self.__height

    def set_height(self, value) -> None:
        if value < 0:
            """Invalid imput. Height can not be negative"""            
        else
            self.__height = value

    def get_age (self) -> int:
        """"Returns the Plant instance height in centimeters"""
        return self.__age

    def set_age (self, value) -> None:
        if value < 0:
            """Invalid imput. Age can not be negative"""            
        else
            self.__age = value

class Flower(Plant):
    """
    Paste Description Here.
    """
    def __init__(self, name: str,height: int, age: int, color: str):
        super(self).__init__(name, height, age):
        self.set_color(self)
    
