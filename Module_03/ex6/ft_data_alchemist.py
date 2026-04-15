"""Game Data Alchemist - Exercise 6.

Demonstrates list and dict comprehensions to transform player names
and build score dictionaries. Outputs average and high-score filter
results in a compact format suitable for evaluation.
"""

import random


PLAYERS: list[str] = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam',
]


def main() -> None:
    """Run the data alchemist demo printing transformed names and scores."""
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS}")
    all_cap = list(name.capitalize() for name in PLAYERS)
    print(f"New list with all names capitalized: {all_cap}")
    only_cap = list(name for name in PLAYERS if name == name.capitalize())
    print(f"New list of capitalized names only: {only_cap}\n")
    score_dict: dict[str, int] = {
        name: random.randint(0, 999)
        for name in all_cap
    }
    print(f"Score dict: {score_dict}")
    average_score = round((sum(score_dict.values()) / len(score_dict)), 2)
    print(f"Score average is {average_score}")
    average_dict = {
        name: score
        for name, score in score_dict.items()
        if score > average_score
    }
    print(f"High scores: {average_dict}")


if __name__ == "__main__":
    main()
