def validate_ingredients(ingredients: str) -> str:
    """Validate whether ingredients contain any allowed spell components.
    Uses deferred import to break the circular dependency with
    light_spellbook — both modules reference each other, but the
    import inside this function ensures light_spellbook is fully
    initialized before we access light_spell_allowed_ingredients.
    """
    from .light_spellbook import light_spell_allowed_ingredients  # deferred
    allowed = light_spell_allowed_ingredients()
    for item in allowed:
        if item in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
