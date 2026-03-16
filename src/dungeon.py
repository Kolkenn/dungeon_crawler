import random
from src.player import Player
from src.monster import MONSTER_TYPES
from src.combat import run_combat

TOTAL_FLOORS = 5 # Total number of floors in the dungeon

class Dungeon:
    def __init__(self):
        self.floor = 1 # Current floor, starts at 1 and increases after each encounter

    def is_complete(self) -> bool:
        '''Returns True if player has cleared all floors, False otherwise.'''
        return self.floor > TOTAL_FLOORS

    def next_encounter(self, player: Player):
        """
        Runs one floor's encounter. For now, each floor just has one monster encounter, but this can be expanded with traps, puzzles, shops, etc.
        """
        print(f"\n=== Floor {self.floor} of {TOTAL_FLOORS} ===")

        # For now, every floor just has one monster encounter.
        monster = self._spawn_monster()
        run_combat(player, monster)

        if player.is_alive():
            self.floor += 1

    def _spawn_monster(self):
        """Randomly selects a monster type and creates an instance of it."""
        monster_types = random.choice(list(MONSTER_TYPES.values()))
        monster_func = random.choice(monster_types)
        return monster_func()
