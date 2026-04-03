class TempError(Exception):
    """
    Custom exception raised when the temperature is outside the
    biologically acceptable limits for the plants (0°C to 40°C).
    """
    pass


def input_temperature(temp_str: str = "N/A") -> int | None:
    """
    Validates the input string representing a temperature.
    Raises TempError if the temperature is not between 0 and 40.

    Args:
        temp_str (str): The temperature value as a string.

    Returns:
        int | None: The integer temperature if valid, or None if
        conversion fails.
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
    if temp < 0:
        print(f"Input data is '{temp}'")
        raise TempError(
                        f"Caught input_temperature error: {temp}°C"
                        " is too cold for plants (min 0°C)"
        )
    if temp > 40:
        print(f"Input data is '{temp}'")
        raise TempError(
                        f"Caught input_temperature error: {temp}°C"
                        " is too hot for plants (max 40°C)"
        )
    print(f"Input data is '{temp}'")
    print(f"Temperature is now {temp}°C")
    return temp


def test_temperature() -> None:
    """
    Runs a battery of tests with normal, invalid, and extreme
    temperature values to verify error handling without crashing.
    """
    input_temperature("25")
    print()
    input_temperature("abc")
    print()
    try:
        input_temperature("100")
    except TempError as e:
        print(e)
    print()
    try:
        input_temperature("-50")
    except TempError as e:
        print(e)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
