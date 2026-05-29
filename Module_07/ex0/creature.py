from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class representing a creature in the card game."""

    def __init__(
        self,
        name: str = "unknown",
        creature_type: str = "normal"
    ) -> None:
        """Initialize a creature with a name and type."""
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Execute the creature's attack and return a description string."""
        pass

    def describe(self) -> str:
        """Return a description of the creature's name and type."""
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    """A Fire-type base creature that uses Ember."""

    def __init__(self) -> None:
        """Initialize a Flameling with its default name and type."""
        super().__init__(name="Flameling", creature_type="Fire")

    def attack(self) -> str:
        """Return the attack description for Ember."""
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """A Fire/Flying-type evolved creature that uses Flamethrower."""

    def __init__(self) -> None:
        """Initialize a Pyrodon with its default name and type."""
        super().__init__(name="Pyrodon", creature_type="Fire/Flying")

    def attack(self) -> str:
        """Return the attack description for Flamethrower."""
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """A Water-type base creature that uses Water Gun."""

    def __init__(self) -> None:
        """Initialize an Aquabub with its default name and type."""
        super().__init__(name="Aquabub", creature_type="Water")

    def attack(self) -> str:
        """Return the attack description for Water Gun."""
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """A Water-type evolved creature that uses Hydro Pump."""

    def __init__(self) -> None:
        """Initialize a Torragon with its default name and type."""
        super().__init__(name="Torragon", creature_type="Water")

    def attack(self) -> str:
        """Return the attack description for Hydro Pump."""
        return f"{self.name} uses Hydro Pump!"
