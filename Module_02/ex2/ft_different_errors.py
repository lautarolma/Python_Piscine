"""
Demonstrate several common exception types via garden operations.

This module provides garden_operations which intentionally raises different
exceptions based on an operation number, and test_error_types which runs
the operations and prints a human-readable description for each exception
type encountered.
"""


def garden_operations(operation_number: int) -> None:
    """
    Perform a dummy garden operation that triggers an exception.

    Args:
        operation_number: Selects which error to raise:
            0 -> ValueError via int("abc")
            1 -> ZeroDivisionError via division by zero
            2 -> FileNotFoundError via opening a non-existent file
            3 -> TypeError via invalid string + int concatenation
            Any other value -> no exception (operation is a no-op)
    """
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        5 / 0
    if operation_number == 2:
        open("/non/existent/file")
    if operation_number == 3:
        "aasd" + 1


def test_error_types() -> None:
    """
    Run garden_operations for a range of operation numbers and handle errors.

    Iterates through several operation numbers, calling garden_operations for
    each. Catches specific exception types and prints descriptive messages so
    the behaviour is visible when running the module as a script.
    """
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError:
            print(
                    "Caught ValueError: invalid literal for int() "
                    "with base 10: 'abc'"
            )
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print(
                    "Caught FileNotFoundError: [Errno 2] No such file or "
                    "directory: '/non/existent/file'"
            )
        except TypeError:
            print(
                    'Caught TypeError: can only concatenate str '
                    '(not "int") to str'
            )
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
