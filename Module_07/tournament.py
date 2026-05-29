from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy
from ex2.exceptions import InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Run a tournament between all pairs of opponents.

    Each opponent is a (factory, strategy) tuple.
    Each pair fights once. If an invalid combination is detected,
    the tournament is aborted with an error message.
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_i, strategy_i = opponents[i]
            factory_j, strategy_j = opponents[j]

            creature_i = factory_i.create_base()
            creature_j = factory_j.create_base()

            print("\n* Battle *")
            print(creature_i.describe())
            print(" vs.")
            print(creature_j.describe())
            print(" now fight!")

            try:
                print(strategy_i.act(creature_i))
                print(strategy_j.act(creature_j))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    """Run the three tournament scenarios."""
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print()

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
