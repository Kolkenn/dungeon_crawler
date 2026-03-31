class Monster:
    def __init__(self, species: str, hp: int, attack: int, defense: int):
        self.species = species
        self.hp = hp
        self.max_hp = hp # Store max HP for display purposes
        self.attack = attack
        self.defense = defense
        self.no_damage_message = "it takes no damage thanks to its armor"

        # Calculate XP dynamically upon instantiation
        self.xp_reward = self._calculate_experience_reward()

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int):
        actual = max(0, amount - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual
    
    def _calculate_experience_reward(self) -> int:
        """Calculates experience reward based on the monster's actual combat stats."""        

        # Apply the weights to the stats
        hp_score = self.max_hp * 0.5
        def_score = self.defense * 4.0
        atk_score = self.attack * 2.0

        # 3. Sum the scores and return as an integer
        total_xp = hp_score + def_score + atk_score
        
        return int(total_xp)

# Undead Monters (Skeletons, Zombies, etc.)
class Undead(Monster):
    def __init__(self, hp: int, attack: int, defense: int):
        super().__init__("Undead", hp, attack, defense)

class Zombie(Undead):
    def __init__(self):
        super().__init__(hp=35, attack=2, defense=1)
        self.species = "Zombie"
        self.no_damage_message = "it considers taking damage but doesn't."
    
class Skeleton(Undead):
    def __init__(self):
        super().__init__(hp=22, attack=5, defense=3)
        self.species = "Skeleton"
        self.no_damage_message = "it takes no damage thanks to its calcium supplements."

class Ghoul(Undead):
    def __init__(self):
        super().__init__(hp=28, attack=6, defense=2)
        self.species = "Ghoul"
        self.no_damage_message = "it takes no damage and drops its jaw, quickly picking it up."

class Lich(Undead):
    def __init__(self):
        super().__init__(hp=40, attack=12, defense=5)
        self.species = "Lich"
        self.no_damage_message = "it takes no damage thanks to the wind under its robe."

# Humanoids (Bandits, Cultists, etc.)
class Humanoid(Monster):
    def __init__(self, hp: int, attack: int, defense: int):
        super().__init__("Humanoid", hp, attack, defense)

class Goblin(Humanoid):
    def __init__(self):
        super().__init__(hp=20, attack=4, defense=1)
        self.species = "Goblin"
        self.no_damage_message = "it takes no damage and laughs at you insultingly."

class Bandit(Humanoid):
    def __init__(self):
        super().__init__(hp=25, attack=5, defense=2)
        self.species = "Bandit"
        self.no_damage_message = "it takes no damage and threatens to steal your wallet."

class HobGoblin(Humanoid):
    def __init__(self):
        super().__init__(hp=30, attack=6, defense=3)
        self.species = "Hobgoblin"
        self.no_damage_message = "it takes no damage and mocks your puny strength."

class BanditKing(Humanoid):
    def __init__(self):
        super().__init__(hp=35, attack=10, defense=3)
        self.species = "Bandit King"
        self.no_damage_message = "it takes no damage and demands to know if you have any gold on you."

# Beasts (Giant Rats, Trolls etc.)
class Beast(Monster):
    def __init__(self, hp: int, attack: int, defense: int):
        super().__init__("Beast", hp, attack, defense)

class GiantRat(Beast):
    def __init__(self):
        super().__init__(hp=18, attack=4, defense=1)
        self.species = "Giant Rat"
        self.no_damage_message = "it takes no damage and squeaks defiantly."

class GiantSpider(Beast):
    def __init__(self):
        super().__init__(hp=22, attack=5, defense=2)
        self.species = "Giant Spider"
        self.no_damage_message = "it takes no damage and stares at you with all eight eyes judgmentally"

class Troll(Beast):
    def __init__(self):
        super().__init__(hp=35, attack=4, defense=3)
        self.species = "Troll"
        self.no_damage_message = "it takes no damage, it's basically just confused by the concept of taking damage."

class Dragon(Beast):
    def __init__(self):
        super().__init__(hp=50, attack=15, defense=5)
        self.species = "Dragon"
        self.no_damage_message = "it takes no damage and snorts at your puny efforts."

# Dictionary mapping monster type names to their corresponding classes for easy instantiation 
GENERAL_MONSTER_TYPES = {
    "humanoid": [Goblin, HobGoblin, Bandit],
    "undead": [Skeleton, Zombie, Ghoul],
    "beast": [Troll, GiantRat, GiantSpider]
}

BOSS_MONSTERS = {
    "humanoid": [BanditKing],
    "undead": [Lich],
    "beast": [Dragon]
}