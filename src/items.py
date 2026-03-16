
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.description}"

class Consumable(Item):
    """Base class for consumable items that can be used by the player."""
    def __init__(self, name: str, description: str):
        super().__init__(name, description)  

    def use(self, player: Player):
        """Defines the effect of using the item on the player. To be implemented by subclasses."""
        raise NotImplementedError("Use method must be implemented by subclasses of Consumable.")

class HealthPotion(Consumable):
    """A simple health potion that restores a fixed amount of HP when used."""
    def __init__(self, heal_amount: int = 15):
        super().__init__(
            name="Health Potion",
            description=f"Restores {heal_amount} HP"
        )
        self.heal_amount = heal_amount

    def use(self, player: Player):
        player.heal(self.heal_amount)
        print(f"  You drink the potion and restore {self.heal_amount} HP.")

class Weapon(Item):
    """Base class for weapons that can be equipped by the player."""
    def __init__(self, name: str, description: str, attack_bonus: int):
        super().__init__(name, description)
        self.attack_bonus = attack_bonus

STARTING_WEAPONS = {
    "Easy": Weapon("Steel Sword", "A sturdy steel sword that increases your attack.", attack_bonus=3),
    "Medium": Weapon("Iron Sword", "A basic iron sword that gives a small attack boost.", attack_bonus=2),
    "Hard": Weapon("Bronze Dagger", "A worn-out bronze dagger that barely increases your attack.", attack_bonus=1)
}

class Armor(Item):
    """Base class for armor that can be equipped by the player."""
    def __init__(self, name: str, description: str, defense_bonus: int):
        super().__init__(name, description)
        self.defense_bonus = defense_bonus

STARTING_ARMOR = {
    "Easy": Armor("Steel Plate Armor", "A set of sturdy steel plates that provide good protection.", defense_bonus=3),
    "Medium": Armor("Iron Plate Armor", "A set of basic iron plates that offer moderate protection.", defense_bonus=2),
    "Hard": Armor("Leather Armor", "A set of worn leather pieces that provide minimal protection.", defense_bonus=1)
}