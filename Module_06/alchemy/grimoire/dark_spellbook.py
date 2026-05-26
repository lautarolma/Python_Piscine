from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the list of allowed ingredients for dark magic spells."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell after validating its ingredients.

    NOTE: importing this module triggers a circular dependency
    (dark_spellbook ↔ dark_validator), raising ImportError.
    """
    validation = validate_ingredients(ingredients)
    return f"Dark spell recorded: {spell_name} ({validation})"
