# Ye Olde Pointless Quest

### _A Journey of Negligible Importance_

A terminal-based roguelike dungeon crawler built in Python. Descend through floors of a dungeon, fight increasingly questionable monsters, level up, and ultimately confront a final boss of debatable menace.

## Setup

```bash
# Clone or download the project, then:
python main.py
```

No external dependencies — standard library only.

## Running Tests

```bash
python -m pytest dungeon_crawler/tests/
```

## Project Structure

```
dungeon_crawler/
├── main.py               # Entry point & game loop
└── src/
    ├── player.py         # Player class (stats, leveling, inventory)
    ├── monster.py        # Monster class + enemy definitions
    ├── combat.py         # Turn-based combat logic
    ├── items.py          # Item base class + HealthPotion
    ├── dungeon.py        # Floor progression & encounter spawning
    └── tests/
        └── test_core.py  # Unit tests
```

## Roadmap / Ideas

- [x] Implement `Player.level_up()`
- [x] Implement the combat loop in `combat.py`
- [x] Implement the main game loop in `main.py`
- [ ] Scale monster difficulty to dungeon floor
- [x] Add a boss fight on the final floor
- [ ] Add loot drops after combat
- [ ] Add more item types (weapons, armor)
- [ ] Add a shop between floors

## Attribution

The initial project boilerplate — including the file structure, class skeletons, stub methods, and unit tests — was generated with the assistance of [Claude](https://claude.ai) (Anthropic). All game logic, combat systems, and gameplay features were written by me.
