class Monster:
    def __init__(self, species: str, hp: int, attack: int, defense: int, xp_reward: int):
        self.species = species
        self.hp = hp
        self.max_hp = hp # Store max HP for display purposes
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.no_damage_message = "it takes no damage thanks to its armor"

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int):
        actual = max(0, amount - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

# Undead Monters (Skeletons, Zombies, etc.)
class Undead(Monster):
    def __init__(self, hp: int, attack: int, defense: int, xp_reward: int):
        super().__init__("Undead", hp, attack, defense, xp_reward)
    
class Skeleton(Undead):
    def __init__(self):
        super().__init__(hp=15, attack=5, defense=2, xp_reward=8)
        self.species = "Skeleton"
        self.no_damage_message = "it takes no damage thanks to its calcium supplements."

class Zombie(Undead):
    def __init__(self):
        super().__init__(hp=20, attack=4, defense=1, xp_reward=10)
        self.species = "Zombie"
        self.no_damage_message = "it considers taking damage but doesn't."

class Ghoul(Undead):
    def __init__(self):
        super().__init__(hp=18, attack=6, defense=2, xp_reward=12)
        self.species = "Ghoul"
        self.no_damage_message = "it takes no damage and drops its jaw, quickly picking it up."

class Lich(Undead):
    def __init__(self):
        super().__init__(hp=40, attack=12, defense=5, xp_reward=25)
        self.species = "Lich"
        self.no_damage_message = "it takes no damage thanks to the wind under its robe."

# Humanoids (Bandits, Cultists, etc.)
class Humanoid(Monster):
    def __init__(self, hp: int, attack: int, defense: int, xp_reward: int):
        super().__init__("Humanoid", hp, attack, defense, xp_reward)

class Goblin(Humanoid):
    def __init__(self):
        super().__init__(hp=10, attack=3, defense=0, xp_reward=5)
        self.species = "Goblin"
        self.no_damage_message = "it takes no damage and laughs at you insultingly."

class HobGoblin(Humanoid):
    def __init__(self):
        super().__init__(hp=20, attack=6, defense=1, xp_reward=12)
        self.species = "Hobgoblin"
        self.no_damage_message = "it takes no damage and mocks your puny strength."

class Bandit(Humanoid):
    def __init__(self):
        super().__init__(hp=18, attack=5, defense=1, xp_reward=10)
        self.species = "Bandit"
        self.no_damage_message = "it takes no damage and threatens to steal your wallet."

class BanditKing(Humanoid):
    def __init__(self):
        super().__init__(hp=35, attack=10, defense=3, xp_reward=20)
        self.species = "Bandit King"
        self.no_damage_message = "it takes no damage and demands to know if you have any gold on you."

# Beasts (Giant Rats, Trolls etc.)
class Beast(Monster):
    def __init__(self, hp: int, attack: int, defense: int, xp_reward: int):
        super().__init__("Beast", hp, attack, defense, xp_reward)

class Troll(Beast):
    def __init__(self):
        super().__init__(hp=25, attack=8, defense=3, xp_reward=15)
        self.species = "Troll"
        self.no_damage_message = "it takes no damage, it's basically just confused by the concept of taking damage."

class GiantRat(Beast):
    def __init__(self):
        super().__init__(hp=8, attack=2, defense=0, xp_reward=3)
        self.species = "Giant Rat"
        self.no_damage_message = "it takes no damage and squeaks defiantly."

class GiantSpider(Beast):
    def __init__(self):
        super().__init__(hp=12, attack=4, defense=1, xp_reward=7)
        self.species = "Giant Spider"
        self.no_damage_message = "it takes no damage and stares at you with all eight eyes judgmentally"

class Dragon(Beast):
    def __init__(self):
        super().__init__(hp=50, attack=15, defense=5, xp_reward=30)
        self.species = "Dragon"
        self.no_damage_message = "it takes no damage and snorts at your puny efforts."

# Dictionary mapping monster type names to their corresponding classes for easy instantiation 
GENERAL_MONSTER_TYPES = {
    "humanoid": [Goblin, HobGoblin, Bandit],
    "undead": [Skeleton, Zombie],
    "beast": [Troll, GiantRat, GiantSpider]
}

BOSS_MONSTERS = {
    "humanoid": [BanditKing],
    "undead": [Lich],
    "beast": [Dragon]
}