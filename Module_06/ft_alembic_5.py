from alchemy import create_air


def main() -> None:
    """Test importing create_air directly from the alchemy package."""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
