"""
"""

def input_temperature(temp_str: str = "N/A") -> int | None:
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
    input_temperature("25")
    print()
    input_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
