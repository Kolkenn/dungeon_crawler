import random

class Player:
    def __init__(self, name: str):
        self.name = name # Player's name
        self.level = 1 # Player's level
        self.xp = 0 # Experience points
        self.xp_to_level = 10 # XP needed to level up, can be increased on level up
        self.max_hp = 30 # Maximum hitpoints, can be increased on level up
        self.hp = self.max_hp # Hitpoints
        self.attack = 5 # Attack stat, can be increased on level up
        self.defense = 2 # Defense stat, can be increased on level up
        self.inventory = [] # List of items player has, can be expanded with item system

    def is_alive(self) -> bool:
        """Returns True if player is alive (hp > 0), False otherwise."""
        return self.hp > 0

    def take_damage(self, amount: int):
        """Calculates damage taken after defense, reduces hp, and returns actual damage taken."""
        actual = max(0, amount - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual  # return actual damage taken (useful for combat messages)

    def heal(self, amount: int):
        """Heals the player by a specified amount, not exceeding their maximum HP."""
        self.hp = min(self.max_hp, self.hp + amount)

    def gain_xp(self, amount: int):
        """Gains experience points and checks for level up."""
        self.xp += amount
        if self.xp >= self.xp_to_level:
            self.level_up()

    def level_up(self):
        """Levels up the player and increases their stats."""
        self.level += 1
        self.hp += 10
        self.max_hp += random.randint(5, 10) # Increase max HP by a random amount
        self.attack += random.randint(1, 3) # Increase attack by a random amount
        self.defense += random.randint(1, 2) # Increase defense by a random amount
        self.xp = 0 # Reset experience points after leveling up
        self.xp_to_level += 10 # Increase experience points needed for next level
        print(f"\nCongratulations! You've reached level {self.level}!")
        print(f"Your stats have increased: HP {self.max_hp}, ATK {self.attack}, DEF {self.defense}.")


    def show_status(self):
        print(f"\n--- {self.name} | Level {self.level} ---")
        print(f"  HP:     {self.hp}/{self.max_hp}")
        print(f"  ATK:    {self.attack}  DEF: {self.defense}")
        print(f"  XP:     {self.xp}/{self.xp_to_level}")
