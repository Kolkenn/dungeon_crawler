import random
from src.player import Player
from src.monster import Monster

def run_combat(player: Player, monster: Monster):
    """
    Runs a turn-based combat loop between player and monster.
    """
    print(f"\nA wild {monster.species} appears!\n")

    # TODO: implement player options (attack, use item, flee)

    # TODO: execute player action and monster response
    # For now, just have them attack each other until one dies to develop the basic combat loop.
    while player.is_alive() and monster.is_alive():
        # For now, player just attacks and monster just attacks back.
        player_attack(player, monster)
        if monster.is_alive():
            monster_attack(monster, player)

    # TODO: resolve outcome (victory, defeat, fled)
    if player.is_alive(): # Victory
        print(f"\nYou defeated the {monster.species}!")
        player.gain_xp(monster.xp_reward)
    else: # Defeat
        print(f"\nYou were slain by the {monster.species}... Game Over.")


def player_attack(player: Player, monster: Monster) -> int:
    """Player attacks monster. Returns damage dealt."""
    damage = player.attack
    actual = monster.take_damage(damage)
    print(f"  You attack the {monster.species} for {actual} damage.")
    return actual


def monster_attack(monster: Monster, player: Player) -> int:
    """Monster attacks player. Returns damage dealt."""
    damage = random.randint(1, monster.attack)
    actual = player.take_damage(damage)
    print(f"  The {monster.species} hits you for {actual} damage!")
    return actual
