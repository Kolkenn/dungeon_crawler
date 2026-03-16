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


def make_goblin() -> Monster:
    """Factory function to create a Goblin monster."""
    return Monster(species="Goblin", hp=10, attack=3, defense=0, xp_reward=5)


def make_skeleton() -> Monster:
    """Factory function to create a Skeleton monster."""
    return Monster(species="Skeleton", hp=15, attack=5, defense=2, xp_reward=8)


def make_troll() -> Monster:
    """Factory function to create a Troll monster."""
    return Monster(species="Troll", hp=25, attack=8, defense=3, xp_reward=15)

MONSTER_TYPES = {
    "goblin": make_goblin,
    "skeleton": make_skeleton,
    "troll": make_troll,
}