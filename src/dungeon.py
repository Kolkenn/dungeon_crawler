import random
from src.player import Player
from src.monster import GENERAL_MONSTER_TYPES,BOSS_MONSTERS
from src.combat import run_combat

TOTAL_FLOORS = 5 # Total number of floors in the dungeon

class Dungeon:
    def __init__(self,num_floors: int = TOTAL_FLOORS):
        self.floor = 1 # Current floor, starts at 1 and increases after each encounter
        self.total_floors = num_floors

    def is_complete(self) -> bool:
        '''Returns True if player has cleared all floors, False otherwise.'''
        return self.floor > self.total_floors

    def next_encounter(self, player: Player):
        """
        Runs one floor's encounter. For now, each floor just has one monster encounter, but this can be expanded with traps, puzzles, shops, etc.
        """
        print(f"\n=== Floor {self.floor} ===")

        # For now, every floor just has one monster encounter.
        monster = self._spawn_monster()
        run_combat(player, monster)

        # TODO: add loot drops, gold rewards, etc.
        # TODO: add choice of furthering deeper or leave and save progress (if we implement saving/loading) after each encounter, especially if player is low on health or resources. Maybe also add a shop encounter every few floors where player can buy healing potions, gear upgrades, etc.

        if player.is_alive():
            self.floor += 1

    def _spawn_monster(self):
        """Randomly selects a monster type and creates an instance of it."""
        if self.floor == self.total_floors: # Spawn a boss on the final floor
            boss_types = random.choice(list(BOSS_MONSTERS.values()))
            boss_func = random.choice(boss_types)
            return boss_func()
        else: # Spawn a regular monster on other floors
            monster_types = random.choice(list(GENERAL_MONSTER_TYPES.values()))
            monster_func = random.choice(monster_types)
            return monster_func()
