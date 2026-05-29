from ex0.factory import CreatureFactory
from ex0.creature import Creature
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """Factory for the healing creature family: Sproutling and Bloomelle."""

    def create_base(self) -> Creature:
        """Create and return a Sproutling."""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Create and return a Bloomelle."""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for the transform creature family: Shiftling and Morphagon."""

    def create_base(self) -> Creature:
        """Create and return a Shiftling."""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Create and return a Morphagon."""
        return Morphagon()
