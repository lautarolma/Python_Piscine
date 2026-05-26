import alchemy.transmutation.recipes


def main() -> None:
    """Test accessing recipes.py directly with full import path."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        "Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
