import sys

"""Reads files and transforms content by adding '#' at the end of each line.

Handles errors for nonexistent files or permission issues."""


def data_preserver(content: str) -> str:
    """Adds '#' to the end of each line.

    Args:
        content: Original content.
    Returns:
        Transformed content with '#' at the end of each line.
    """
    lines = content.splitlines()
    return '\n'.join(line + '#' for line in lines) + '\n'


def main():
    """Entry point. Reads file, transforms content and asks where to save."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
        content = file.read()
        print("---\n")
        print(content)
        print("---")
    except FileNotFoundError:
        print(
                f"Error opening file '{file_name}': [Errno 2] No such"
                f" file or directory: '{file_name}'"
        )
        return
    except PermissionError:
        print(
                f"Error opening file '{file_name}': [Errno 13]"
                f" Permission denied: '{file_name}'"
        )
        return
    except (IsADirectoryError, OSError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    finally:
        try:
            file.close()
            print(f"File '{file_name}' closed.")
        except NameError:
            pass
    print("Transform data:")
    new_content = data_preserver(content)
    print(new_content)
    file_name = input("Enter new file name (or empty): ")
    if not file_name:
        print("Not saving data.")
        return
    try:
        new_file = open(file_name, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Saving data to '{file_name}'")
        print(f"Data saved in file '{file_name}'.")
    except (PermissionError, OSError) as e:
        print(f"Error opening file '{file_name}': {e}")
        print("Data not saved.")


if __name__ == "__main__":
    main()
