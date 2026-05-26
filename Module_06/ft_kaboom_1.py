def main() -> None:
    """Trigger the circular import and let it explode."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: F401


if __name__ == "__main__":
    main()
