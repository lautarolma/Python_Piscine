"""Player Score Analytics.

Process numeric scores provided as command-line arguments and print
basic statistics: total, average, max, min and range. Invalid numeric
parameters are reported and ignored. Outputs a short usage message
if no valid scores are provided.
"""

import sys


def ft_score_analytics() -> None:
    """Parse command-line scores and print analytics summary.

    Reads sys.argv for integer scores, reports invalid parameters,
    and prints the computed metrics when at least one valid score is
    available. Does not return a value.
    """
    print("=== Player Score Analytics ===")
    args: list[str] = sys.argv
    scores: list[int] = []
    for nb in args[1:]:
        try:
            scores.append(int(nb))
        except ValueError:
            print(f"Invalid parameter: '{nb}'")
    if len(scores) == 0:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ..."
        )
        return
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
