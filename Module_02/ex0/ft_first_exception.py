"""
Utilities for demonstrating basic exception handling for garden temperature.

This module provides a small helper to parse temperatures from strings
and a simple test runner that shows successful and failing conversions.
"""


def input_temperature(temp_str: str = "N/A") -> int | None:
    """
    Parse a temperature string to an integer.

    Attempts to convert `temp_str` to an int. On success prints diagnostic
    messages and returns the parsed integer. If conversion fails due to
    TypeError or ValueError, prints an explanatory message and returns None.

    Args:
        temp_str: The input value to convert to an integer. Defaults to "N/A".

    Returns:
        The parsed temperature as int on success, otherwise None.
    """
    try:
        temp = int(temp_str)
    except (TypeError, ValueError):
        print(f"Input data is '{temp_str}'")
        print(
            "Caught input_temperature error: invalid literal for int() "
            f"with base 10: '{temp_str}'"
        )
        return None
    else:
        print(f"Input data is '{temp}'")
        print(f"Temperature is now {temp}°C")
        return temp


def test_temperature() -> None:
    """
    Execute simple manual tests for input_temperature.

    Calls input_temperature with a valid numeric string and a non-numeric
    string to demonstrate normal and error handling behaviour. Intended to be
    run when the module is executed as a script.
    """
    input_temperature("25")
    print()
    input_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
