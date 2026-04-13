import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    args: list = sys.argv
    scores = []
    for nb in args[1:]:
        try:
            scores.append(int(nb))
        except ValueError:
            print(f"Invalid parameter: '{nb}'")
    if len(scores) == 0:
        print(
                "No scores provided. Usage: python3 ft_score_analytics.py"
                "<score1> <score2> ..."
        )
    if len(scores) > 0:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        average_score = sum(scores) / len(scores)
        print(f"Average score: {average_score}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        score_range = (max(scores) - min(scores))
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
