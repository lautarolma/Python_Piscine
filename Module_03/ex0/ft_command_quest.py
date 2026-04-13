import sys


def ft_command_quest():
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print(f"Program name: {sys.argv[0]}")
        print("No arguments provided!")
        print("Total arguments: 1")
    if len(sys.argv) > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments recived: {(len(sys.argv) - 1)}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
