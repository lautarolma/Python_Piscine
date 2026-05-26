import alchemy


def main() -> None:
    """Test that create_air is exposed but create_earth is hidden."""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print(f"Testing create_earth: {alchemy.create_earth()}")
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    main()
