"""Command Quest script.

Simple script to display command-line parameters and basic stats.
Designed for the Data Quest exercises: shows program name,
the number of arguments and each argument when provided.
Keeps output concise and easy to inspect during evaluation.
"""

import sys


def ft_command_quest() -> None:
    """Print command-line arguments information.

    Prints a header, the program name, and either a message when no
    additional arguments are provided or a numbered list of the
    provided arguments. This function does not return a value.
    """
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print(f"Program name: {sys.argv[0]}")
        print("No arguments provided!")
        print("Total arguments: 1")
    if len(sys.argv) > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {(len(sys.argv) - 1)}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
