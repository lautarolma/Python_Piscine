"""Alternate implementation for Exercise 3 - Achievement utilities.

Provides the same utility functions as the main tracker but with
slightly different naming. Useful for testing and demonstration.
"""

import random

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
    """Generate random achievements for a player."""
    n_achievements = random.randint(5, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, n_achievements))


def get_all_achievements(player_ach: dict[str, set[str]]) -> set[str]:
    """Get all distinct achievements across all players."""
    all_players_ach: set[str] = set()
    for achievements in player_ach.values():
        all_players_ach = all_players_ach.union(achievements)
    return all_players_ach


def get_common_achievements(players_ach: dict[str, set[str]]) -> set[str]:
    """Get achievements shared by all players."""
    players_list = list(players_ach.keys())
    common_ach: set[str] = players_ach[players_list[0]]
    for achievements in players_ach.values():
        common_ach = common_ach.intersection(achievements)
    return common_ach


def get_only_player_has(
        player: str,
        players_ach: dict[str, set[str]]
) -> set[str]:
    """Get achievements only this player has."""
    player_achievement: set[str] = players_ach[player]
    others_achievement: set[str] = set()
    for other_player, achievements in players_ach.items():
        if other_player != player:
            others_achievement = others_achievement.union(achievements)
    return player_achievement.difference(others_achievement)


def get_missing_achievements(
        player: str,
        all_achievements: set[str],
        players_ach: dict[str, set[str]]
) -> set[str]:
    """Get achievements missing for a player."""
    return all_achievements.difference(players_ach[player])


def main() -> None:
    """Main function for the Achievement Tracker System."""
    print("=== Achievement Tracker System ===\n")

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    players_ach: dict[str, set[str]] = {}

    for player in players:
        players_ach[player] = gen_player_achievements()
        print(f"Player {player}: {players_ach[player]}")

    all_achievements = get_all_achievements(players_ach)
    print(f"\nAll distinct achievements: {all_achievements}")
    common = get_common_achievements(players_ach)
    print(f"\nCommon achievements: {common}\n")
    for player in players:
        only_has = get_only_player_has(
            player, players_ach
        )
        print(f"Only {player} has: {only_has}")
    print()
    for player in players:
        missing = get_missing_achievements(
            player, all_achievements, players_ach
        )
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
