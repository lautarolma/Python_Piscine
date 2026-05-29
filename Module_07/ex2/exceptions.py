class InvalidStrategyError(Exception):
    """
    Raised when act() is called with a creature incompatible with
    the strategy.
    """

    def __init__(self, creature_name: str, strategy_name: str) -> None:
        self.creature_name = creature_name
        self.strategy_name = strategy_name
        super().__init__(
            f"Invalid Creature '{creature_name}' for this {strategy_name}"
            "strategy"
        )
