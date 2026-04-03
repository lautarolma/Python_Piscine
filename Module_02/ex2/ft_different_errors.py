def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        5 / 0
    if operation_number == 2:
        open("/non/existent/file")
    if operation_number == 3:
        "aasd" + 1


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError:
            print(
                    "Caught ValueError: invalid literal for int() "
                    "with base 10: 'abc'"
            )
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError as e:
            print(
                    "Caught FileNotFoundError: [Errno 2] No such file or "
                    "directory: '/non/existent/file'"
            )
        except TypeError as e:
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
    
