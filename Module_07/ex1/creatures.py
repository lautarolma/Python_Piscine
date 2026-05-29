from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """A Grass-type creature with basic healing capability."""

    def __init__(self) -> None:
        super().__init__(name="Sproutling", creature_type="Grass")

    def attack(self) -> str:
        """Return the attack description for Vine Whip."""
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Creature | None = None) -> str:
        """Heal for a small amount and return a description string."""
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """A Grass/Fairy-type evolved creature with strong healing capability."""

    def __init__(self) -> None:
        super().__init__(name="Bloomelle", creature_type="Grass/Fairy")

    def attack(self) -> str:
        """Return the attack description for Petal Dance."""
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Creature | None = None) -> str:
        """Heal for a large amount and return a description string."""
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """A Normal-type creature that can shift into a sharper form."""

    def __init__(self) -> None:
        super().__init__(name="Shiftling", creature_type="Normal")
        self._transformed = False

    def attack(self) -> str:
        """Return the attack description, boosted if transformed."""
        if self._transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Shift into a sharper form and return a description string."""
        self._transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        """Return to normal form and return a description string."""
        self._transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """
    A Normal/Dragon-type evolved creature that morphs into a dragonic form.
    """

    def __init__(self) -> None:
        super().__init__(name="Morphagon", creature_type="Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        """Return the attack description, devastating if transformed."""
        if self._transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """
        Morph into a dragonic battle form and return a description string.
        """
        self._transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Stabilize back to normal form and return a description string."""
        self._transformed = False
        return f"{self.name} stabilizes its form."
