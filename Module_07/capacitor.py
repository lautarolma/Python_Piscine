from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    """Run the capacitor.py test script for the ex1 package."""
    # mypy flags heal()/transform()/revert() as missing on Creature because
    # it only reads static type hints (Creature), not runtime types. The
    # factories return Creature statically, but at runtime they create
    # concrete creatures with capability mixins — mypy can't know that.
    print("Testing Creature with healing capability")
    print(" base:")

    healing = HealingCreatureFactory()
    h_base = healing.create_base()
    print(h_base.describe())
    print(h_base.attack())
    # mypy: Creature type has no "heal" — static hints say Creature, but
    # runtime type (Sproutling) inherits HealCapability.
    print(h_base.heal())

    print(" evolved:")
    h_evolved = healing.create_evolved()
    print(h_evolved.describe())
    print(h_evolved.attack())
    print(h_evolved.heal())

    print("\nTesting Creature with transform capability")
    transform = TransformCreatureFactory()
    t_base = transform.create_base()
    print(" base:")
    print(t_base.describe())
    print(t_base.attack())
    # mypy: same pattern — static type is Creature, runtime type has
    # TransformCapability methods.
    print(t_base.transform())
    print(t_base.attack())
    print(t_base.revert())

    t_evolved = transform.create_evolved()
    print(" evolved:")
    print(t_evolved.describe())
    print(t_evolved.attack())
    print(t_evolved.transform())
    print(t_evolved.attack())
    print(t_evolved.revert())


if __name__ == "__main__":
    main()
