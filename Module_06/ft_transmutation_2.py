import alchemy


def main() -> None:
    """Test accessing lead_to_gold through the top-level alchemy package."""
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")


if __name__ == "__main__":
    main()
