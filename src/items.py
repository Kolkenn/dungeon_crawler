from src.player import Player


class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def use(self, player: Player):
        # TODO: override in subclasses
        raise NotImplementedError(f"{self.name} has no use() defined.")

    def __str__(self):
        return f"{self.name} - {self.description}"


class HealthPotion(Item):
    def __init__(self, heal_amount: int = 15):
        super().__init__(
            name="Health Potion",
            description=f"Restores {heal_amount} HP"
        )
        self.heal_amount = heal_amount

    def use(self, player: Player):
        player.heal(self.heal_amount)
        print(f"  You drink the potion and restore {self.heal_amount} HP.")


# TODO: add more item types — weapons, armor, scrolls, etc.
