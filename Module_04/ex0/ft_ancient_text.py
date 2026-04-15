import sys

"""
Gets the name of a file from the command line, then read the file’s contents
and display them as the cat command would.

It handle the various failure cases (nonexistent files, inaccessible files,
etc.)
"""


def main():
    """Entry point. Reads file from argv and displays its content."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
        content = file.read()
        print("---\n")
        print(content)
        print("---")
        file.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError:
        print(
                f"Error opening file '{file_name}': [Errno 2] No such"
                f" file or directory: '{file_name}'"
        )
    except PermissionError:
        print(
                f"Error opening file '{file_name}': [Errno 13]"
                f" Permission denied: '{file_name}'"
        )


if __name__ == "__main__":
    main()
