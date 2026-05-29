from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    """Mixin abstract class for creatures that can heal."""

    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        """Heal the target (or self) and return a description string."""
        pass


class TransformCapability(ABC):
    """Mixin abstract class for creatures that can transform."""

    @abstractmethod
    def transform(self) -> str:
        """Transform into an enhanced form and return a description string."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revert to the normal form and return a description string."""
        pass
