from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate whether ingredients contain any allowed dark components."""
    allowed = dark_spell_allowed_ingredients()
    for item in allowed:
        if item in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
