from elements import create_water


def main() -> None:
    """Test importing elements.py with 'from ... import ...'."""
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
