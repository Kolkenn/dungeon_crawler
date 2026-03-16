from src.player import Player
from src.dungeon import Dungeon


def main():
    print("==============================================")
    print("       YE OLDE POINTLESS QUEST")
    print("   A Journey of Negligible Importance")
    print("==============================================\n")
    #name = input("Enter your hero's name: ").strip()
    name = "Peter"
    player = Player(name)
    dungeon = Dungeon()

    choice = input("Are you ready to enter the dungeon? Y/N : ")
    if choice.capitalize() == "Y":
        player.show_status()
        print("\nEntering the dungeon...")
        while player.is_alive() and not dungeon.is_complete():
            dungeon.next_encounter(player)
            if player.is_alive():
                player.show_status()
    else:
        print(f"\nFarewell, {player.name}. The pointless quest awaits...")


if __name__ == "__main__":
    main()
