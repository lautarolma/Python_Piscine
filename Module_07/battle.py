from ex0 import FlameFactory, AquaFactory


def main() -> None:
    """Run the battle.py test script for the ex0 package."""
    print("Testing factory")
    flame_factory = FlameFactory()
    f_base = flame_factory.create_base()
    print(f_base.describe())
    print(f_base.attack())
    f_evolved = flame_factory.create_evolved()
    print(f_evolved.describe())
    print(f_evolved.attack())

    print("\nTesting factory")
    aqua_factory = AquaFactory()
    a_base = aqua_factory.create_base()
    print(a_base.describe())
    print(a_base.attack())
    a_evolved = aqua_factory.create_evolved()
    print(a_evolved.describe())
    print(a_evolved.attack())

    print("\nTesting battle")
    print(f_base.describe())
    print(" vs.")
    print(a_base.describe())
    print(" fight!")
    print(f_base.attack())
    print(a_base.attack())


if __name__ == "__main__":
    main()
