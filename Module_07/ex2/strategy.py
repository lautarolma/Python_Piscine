from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    """Abstract strategy defining the battle behavior for a creature."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Check whether the creature is compatible with this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Execute the strategy's battle actions for the given creature.

        Raises InvalidStrategyError if the creature is not compatible.
        """
        pass


class NormalStrategy(BattleStrategy):
    """Strategy suitable for any creature. Simply attacks."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """Strategy suitable for creatures with transform capability.
    Transforms, attacks, then reverts.
    """

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "aggressive")
        # mypy is a static type checker — it reads type hints, not runtime
        # logic. is_valid() does a runtime isinstance check, but mypy cannot
        # "see" across method boundaries, so it flags transform()/revert() as
        # missing on Creature. The code is correct: only creatures that pass
        # is_valid() reach here at runtime.
        return (
            f"{creature.transform()}\n{creature.attack()}"
            f"\n{creature.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    """Strategy suitable for creatures with healing capability.
    Attacks then heals.
    """

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "defensive")
        # Same rationale: mypy can't see that is_valid() guarantees runtime
        # safety. Static type checking cannot track runtime isinstance guards
        # that live in separate methods.
        return f"{creature.attack()}\n{creature.heal()}"
