import sys

"""
Safely reads or writes a file using a context manager.
Handles errors for nonexistent files or permission issues.
"""


def secure_archive(
    file_name: str,
    action: str,
    content: str | None = None,
) -> tuple[bool, str]:
    """Safely reads or writes a file.

    Args:
        file_name: Name of the file to access.
        action: Either "read" or "write".
        content: Content to write if action is "write".

    Returns:
        Tuple with (success: bool, result: str).
    """
    if not file_name or not file_name.strip():
        return (False, "Filename is required")
    if action:
        action = action.lower()
    else:
        action = "read"
    if action == "read":
        try:
            with open(file_name, "r") as file:
                return (True, file.read())
        except (
            FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            OSError,
        ) as e:
            return (False, f"{e}")

    if action == "write":
        if not content:
            return (False, "Content is required for write action")
        try:
            with open(file_name, "w") as new_file:
                new_file.write(content)
            return (True, "'Content successfully written to file'")
        except (PermissionError, OSError) as e:
            return (False, f"{e}")

    if action not in ("read", "write"):
        return (False, f"Invalid action: {action}")

    return (False, "Unknown error")


def main() -> None:
    """Entry point. Uses CLI arguments or runs test cases."""
    if len(sys.argv) < 2:
        print("=== Cyber Archives Security ===\n")
        print("Using 'secure_archive' to read from a nonexistent file:")
        test1 = secure_archive("/not/existing/file", "read")
        print(test1)
        print("\nUsing 'secure_archive' to read from an inaccessible file:")
        test2 = secure_archive("/etc/master.passwd", "read")
        print(test2)
        print("\nUsing 'secure_archive' to read from a regular file:")
        test3 = secure_archive("../ex0/ancient_fragment.txt", "read")
        print(test3)
        print("\nUsing 'secure_archive' to write to a new file:")
        content = "Content successfully written to file\n"
        test4 = secure_archive("new_file", "write", content)
        print(test4)
        return

    filename = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else "read"
    write_content: str | None = sys.argv[3] if len(sys.argv) > 3 else None
    result = secure_archive(filename, action, write_content)
    print(result)


if __name__ == "__main__":
    main()
