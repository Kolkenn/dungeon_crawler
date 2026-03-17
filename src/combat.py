from time import sleep
import random
from src.player import Player
from src.monster import Monster

def run_combat(player: Player, monster: Monster):
    """
    Runs a turn-based combat loop between player and monster.
    """
    print(f"\nA wild {monster.species} appears!\n")

    round = 1
    while player.is_alive() and monster.is_alive():
        # TODO: implement other player options (defend & user item)
        print(f"\n--- Round {round} ---")
        # choice = input("> [A]ttack [F]lee | ")
        choice = "A" # TODO: remove this hardcoding after testing
        match choice.capitalize():
            case "A":
                player_attack(player, monster)
                if monster.is_alive():
                    monster_attack(monster, player)
            case "F":
                print("\nYou fled from the battle! Coward!")
                player.fled_status = True # For now, fleeing just ends the game. TODO: implement fleeing mechanics (chance to escape, consequences of fleeing, etc.)
                return
            case _:
                print("Invalid choice.")        
        round += 1

    # TODO: resolve outcome (victory, defeat, fled)
    if player.is_alive(): # Victory
        print(f"\nYou defeated the {monster.species}!")
        player.gain_xp(monster.xp_reward)
        sleep(1.5) # Pause to let the player read the victory message before clearing the screen for the next encounter
    else: # Defeat
        print(f"\nYou were slain by the {monster.species}... Game Over.")

def player_attack(player: Player, monster: Monster):
    """The player attacks the monster. Calculates damage based on player's attack stat and equipped weapon, applies it to the monster, and prints the result."""
    critical = False
    raw_roll = roll_dice(1, 20) # Roll a D20 to determine if the attack hits, and if it's a critical hit.
    if raw_roll == 20:
        print(f"  Critical hit! You rolled a natural 20! Double damage!")
        critical = True
    player_hit_roll = raw_roll + player.attack
    monster_evasion = roll_dice(1, 20) + monster.defense

    if player_hit_roll < monster_evasion:
        print(f"  You rolled a {player_hit_roll}! Your attack misses the {monster.species}!")
        return
    
    damage = roll_dice(1, player.attack_strength())
    if critical:
        damage *= 2
    damage_taken = monster.take_damage(damage)
    if damage_taken == 0:
        print(f"  You rolled {player_hit_roll} - hits! Your {player.equipment['weapon'].name} hits the {monster.species} for {damage} damage but {monster.no_damage_message} ({monster.hp}/{monster.max_hp} HP)")
    else:
        print(f"  You rolled {player_hit_roll} - hits! Your {player.equipment['weapon'].name} hits the {monster.species} for {damage_taken} damage. ({monster.hp}/{monster.max_hp} HP)")

def monster_attack(monster: Monster, player: Player):
    """Monster attacks player. Calculates damage based on monster's attack stat, applies it to the player, and prints the result."""
    critical = False
    raw_roll = roll_dice(1, 20) # Roll a D20 to determine if the attack hits, and if it's a critical hit.
    if raw_roll == 20:
        print(f"  Critical hit! The {monster.species} rolled a natural 20! Double damage!")
        critical = True
    monster_hit_roll = raw_roll + monster.attack
    player_evasion = roll_dice(1, 20) + player.defense

    if monster_hit_roll < player_evasion:
        print(f"  The {monster.species} rolled a {monster_hit_roll}! Its attack misses you!")
        return

    damage = roll_dice(1, monster.attack)
    if critical:
        damage *= 2
    actual = player.take_damage(damage)
    if actual == 0:
        print(f"  The {monster.species} rolled {monster_hit_roll} - hits! It tries to hit you for {damage} damage but you take no damage thanks to your armor!")
    else:
        print(f"  The {monster.species} rolled {monster_hit_roll} - hits! You take {actual} damage! ({player.hp}/{player.max_hp} HP)")

def roll_dice(num_dice: int, sides: int) -> int:
    """Rolls a specified number of dice with a specified number of sides and returns the total."""
    return sum(random.randint(1, sides) for _ in range(num_dice))