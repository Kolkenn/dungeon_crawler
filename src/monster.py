class Monster:
    def __init__(self, species: str, hp: int, attack: int, defense: int, xp_reward: int):
        self.species = species
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward

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

class Lich(Undead):
    def __init__(self):
        super().__init__(hp=40, attack=12, defense=5, xp_reward=25)
        self.species = "Lich"

class Zombie(Undead):
    def __init__(self):
        super().__init__(hp=20, attack=4, defense=1, xp_reward=10)
        self.species = "Zombie"

# Humanoids (Bandits, Cultists, etc.)
class Humanoid(Monster):
    def __init__(self, hp: int, attack: int, defense: int, xp_reward: int):
        super().__init__("Humanoid", hp, attack, defense, xp_reward)

class Goblin(Humanoid):
    def __init__(self):
        super().__init__(hp=10, attack=3, defense=0, xp_reward=5)
        self.species = "Goblin"

class HobGoblin(Humanoid):
    def __init__(self):
        super().__init__(hp=20, attack=6, defense=1, xp_reward=12)
        self.species = "Hobgoblin"

class Bandit(Humanoid):
    def __init__(self):
        super().__init__(hp=18, attack=5, defense=1, xp_reward=10)
        self.species = "Bandit"

# Beasts (Giant Rats, Trolls etc.)
class Beast(Monster):
    def __init__(self, hp: int, attack: int, defense: int, xp_reward: int):
        super().__init__("Beast", hp, attack, defense, xp_reward)

class Troll(Beast):
    def __init__(self):
        super().__init__(hp=25, attack=8, defense=3, xp_reward=15)
        self.species = "Troll"

class GiantRat(Beast):
    def __init__(self):
        super().__init__(hp=8, attack=2, defense=0, xp_reward=3)
        self.species = "Giant Rat"

class GiantSpider(Beast):
    def __init__(self):
        super().__init__(hp=12, attack=4, defense=1, xp_reward=7)
        self.species = "Giant Spider"

# Dictionary mapping monster type names to their corresponding classes for easy instantiation 
MONSTER_TYPES = {
    "humanoid": [Goblin, HobGoblin, Bandit],
    "undead": [Skeleton, Zombie, Lich],
    "beast": [Troll, GiantRat, GiantSpider]
}