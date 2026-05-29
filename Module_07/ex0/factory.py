from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating base and evolved creatures by family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return a base-form creature."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return an evolved-form creature."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for the Fire creature family: Flameling and Pyrodon."""

    def create_base(self) -> Creature:
        """Create and return a Flameling."""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Create and return a Pyrodon."""
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the Water creature family: Aquabub and Torragon."""

    def create_base(self) -> Creature:
        """Create and return an Aquabub."""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Create and return a Torragon."""
        return Torragon()
