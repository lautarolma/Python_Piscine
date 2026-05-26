from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return the list of allowed ingredients for light magic spells."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell after validating its ingredients."""
    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
