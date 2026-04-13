"""
Achievement Tracker System
Mastering Python Collections - Exercise 3
"""

import random


# Constants
ALL_ACHIEVEMENTS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    """
    Generate a random set of achievements for a player.
    Returns a set with a random number of achievements from the full list.
    """
    num_achievements = random.randint(5, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, num_achievements))


def get_all_distinct_achievements(
    player_achievements: dict[str, set[str]]
) -> set[str]:
    """
    Get all distinct achievements across all players using union.
    """
    all_distinct: set[str] = set()
    for achievements in player_achievements.values():
        all_distinct = all_distinct.union(achievements)
    return all_distinct


def get_common_achievements(
    player_achievements: dict[str, set[str]]
) -> set[str]:
    """
    Get achievements shared by all players using intersection.
    """
    players = list(player_achievements.keys())
    common = player_achievements[players[0]]
    for achievements in player_achievements.values():
        common = common.intersection(achievements)
    return common


def get_only_player_has(
    player: str, player_achievements: dict[str, set[str]]
) -> set[str]:
    """
    Get achievements that only this player has (no one else).
    Uses difference between player's achievements and union of others.
    """
    player_set = player_achievements[player]

    # Union of all OTHER players' achievements
    others_achievements: set[str] = set()
    for other_player, achievements in player_achievements.items():
        if other_player != player:
            others_achievements = others_achievements.union(achievements)

    # What only this player has = player's - others
    return player_set.difference(others_achievements)


def get_missing_achievements(
    player: str,
    all_achievements: set[str],
    player_achievements: dict[str, set[str]]
) -> set[str]:
    """
    Get achievements that this player is missing to have all achievements.
    """
    return all_achievements.difference(player_achievements[player])


def main() -> None:
    """Main function to run the Achievement Tracker System."""
    print("=== Achievement Tracker System ===")

    # Initialize players and their achievements
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements: dict[str, set[str]] = {}

    for player in players:
        player_achievements[player] = gen_player_achievements()
        print(f"Player {player}: {player_achievements[player]}")

    print()

    # All distinct achievements
    all_distinct = get_all_distinct_achievements(player_achievements)
    print(f"All distinct achievements: {all_distinct}")
    print()

    # Common achievements (shared by all players)
    common = get_common_achievements(player_achievements)
    print(f"Common achievements: {common}")
    print()

    # Only each player has
    for player in players:
        only_has = get_only_player_has(player, player_achievements)
        print(f"Only {player} has: {only_has}")

    print()

    # Missing achievements for each player
    for player in players:
        missing = get_missing_achievements(
            player, all_distinct, player_achievements
        )
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
