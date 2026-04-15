"""Game Data Stream Processor - Exercise 5.

Demonstrates generator usage: an infinite event generator and a
consumer that yields items randomly removed from a list. Keeps
output readable for evaluation and avoids storing unnecessary data.
"""

import random
from typing import Generator


# Players and actions available in the game
PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Infinite generator yielding random (player, action) tuples.

    Yields one random (player, action) tuple each time next() is called.
    Does not store anything in memory - produces on demand.
    """
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Yield items by randomly removing them from a list until empty.

    Useful to demonstrate consuming a finite collection with a
    generator without allocating additional structures.
    """
    while events_list:
        idx = random.randint(0, len(events_list) - 1)
        evento = events_list.pop(idx)
        yield evento


def main() -> None:
    """Run generator demo: print 1000 events and consume a small list."""
    print("=== Game Data Stream Processor ===")

    # Generate 1000 events - using next() 1000 times
    gen = gen_event()
    for i in range(1000):
        evento = next(gen)
        print(f"Event {i}: Player {evento[0]} did action {evento[1]}")

    # Build a list of 10 events
    gen2 = gen_event()
    ten_events = [next(gen2) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    # Consume events from the list using the generator
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
