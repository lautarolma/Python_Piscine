import random


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
    "use"
]


def gen_event():
    """Generator of events: infinite stream of (name, action) tuples.

    Yields one random (player, action) tuple each time next() is called.
    Does not store anything in memory - produces on demand.
    """
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(events_list):
    """Generator that consumes events from a list by random selection.

    Each time next() is called, picks a random index, removes the event
    from the list, and yields it. Stops when the list is empty.

    Args:
        events_list: List of (name, action) tuples to consume.

    Yields:
        Tuple (name, action) removed from the list.
    """
    while events_list:
        idx = random.randint(0, len(events_list) - 1)
        evento = events_list.pop(idx)
        yield evento


if __name__ == "__main__":
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
