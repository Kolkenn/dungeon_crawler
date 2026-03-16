import random
from src.items import STARTING_ARMOR, STARTING_WEAPONS

class Player:
    def __init__(self, name: str, difficulty: str):
        self.name = name # Player's name
        self.level = 1 # Player's level
        self.xp = 0 # Experience points
        self.xp_to_level = 10 # XP needed to level up, can be increased on level up
        
        self.max_hp = 30 # Maximum hitpoints, can be increased on level up
        self.hp = self.max_hp # Hitpoints
        self.attack = None # Attack stat (damage dealt), can be increased on level up
        self.defense = None # Defense stat (damage reduction), can be increased on level up
        self.equipment = {
            "weapon": None,
            "armor": None
        } # Dict of equipped items, can be expanded with equipment system
        self._stat_and_gear_setup(difficulty)

    def _stat_and_gear_setup(self, difficulty: str):
        """Sets initial stats and gear based on chosen difficulty."""
        match difficulty.lower():
            case "easy":
                self.attack = 5
                self.defense = 4
                self.equipment["weapon"] = STARTING_WEAPONS["Easy"]
                self.equipment["armor"] = STARTING_ARMOR["Easy"]
            case "medium":
                self.attack = 4
                self.defense = 3
                self.equipment["weapon"] = STARTING_WEAPONS["Medium"]
                self.equipment["armor"] = STARTING_ARMOR["Medium"]
            case "hard":
                self.attack = 3
                self.defense = 2
                self.equipment["weapon"] = STARTING_WEAPONS["Hard"]
                self.equipment["armor"] = STARTING_ARMOR["Hard"]
            case _:
                raise ValueError("Invalid difficulty level. Choose Easy, Medium, or Hard.")
    
    def is_alive(self) -> bool:
        """Returns True if player is alive (hp > 0), False otherwise."""
        return self.hp > 0

    def take_damage(self, amount: int):
        """Calculates damage taken after defense, reduces hp, and returns actual damage taken."""
        armor_bonus = self.equipment["armor"].defense_bonus if self.equipment["armor"] else 0
        actual = max(0, amount - (self.defense + armor_bonus)) # Damage is reduced by defense and armor but not below 0
        self.hp = max(0, self.hp - actual)
        return actual  # return actual damage taken (useful for combat messages)
    
    def deal_damage(self) -> int:
        """Calculates damage dealt based on attack stat and equipped weapon."""
        weapon_bonus = self.equipment["weapon"].attack_bonus if self.equipment["weapon"] else 0
        return self.attack + weapon_bonus

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
        self.heal(10) # Heal the player 10 hitpoints on level up
        self.max_hp += random.randint(5, 10) # Increase max HP by a random amount
        self.attack += random.randint(1, 3) # Increase attack by a random amount
        self.defense += random.randint(1, 2) # Increase defense by a random amount
        self.xp = self.xp - self.xp_to_level # Subtract the XP needed for level up from current XP to allow for carryover
        self.xp_to_level += 10 # Increase experience points needed for next level
        print(f"\nCongratulations! You've reached level {self.level}!")
        print(f"Your stats have increased: HP {self.max_hp}, ATK {self.attack}, DEF {self.defense}. You feel stronger and more prepared for the challenges ahead.")

    def show_status(self):
        print(f"\n--- {self.name} | Level {self.level} ---")
        print(f"  HP:     {self.hp}/{self.max_hp}")
        print(f"  ATK:    {self.attack}  DEF: {self.defense}")
        print(f"  XP:     {self.xp}/{self.xp_to_level}")
        print(f"  Weapon: {self.equipment['weapon'].name} | Armor: {self.equipment['armor'].name}")
