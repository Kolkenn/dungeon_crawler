import subprocess

from src.player import Player
from src.dungeon import Dungeon


def main():
    print("="* 40)
    print("       YE OLDE POINTLESS QUEST")
    print("   A Journey of Negligible Importance")
    print("="* 40)
    print("\n")
    
    # Name input loop with validation to prevent empty names
    # while True:
    #     name = input("Enter your hero's name: ").strip()
    #     if name:
    #         break
    #     else:
    #         print("A hero must have a name or else how will we know when he dies! Please enter a valid name.")
    name = "Peter" # TODO: remove this hardcoding after testing

    print(f"Welcome, {name}! Your quest, should you choose to accept it, is to delve into the depths of the dungeon and emerge victorious. But beware, danger lurks around every corner!")
    print("Choose your difficulty level wisely, as it will affect your starting stats and gear. Good luck, brave adventurer!\n")
    
    # Choice loop for difficulty selection, with input validation
    # while True:
    #     difficulty = input("Choose your difficulty (Easy/Medium/Hard): ").strip()
    #     if difficulty.lower() in ["easy", "medium", "hard"]:
    #         break
    #     else:
    #         print("That wasn't an option you cheeky dog. Please enter Easy, Medium, or Hard.")
    difficulty = "medium" # TODO: remove this hardcoding after testing

    # Initialize Player and Dungeon Objects
    player = Player(name, difficulty)
    dungeon = Dungeon()

    # Main Loop: runs until player dies, completes the dungeon, or flees (TODO)
    # choice = input("Are you ready to enter the dungeon? Y/N : ")
    choice = "Y" # TODO: remove this hardcoding after testing
    if choice.capitalize() == "Y":
        player.show_status()
        print("\nEntering the dungeon...")
        while player.is_alive() and not dungeon.is_complete() and not player.fled():
            dungeon.next_encounter(player)
            if player.is_alive() and not player.fled():
                # subprocess.run("cls",shell=True) # Clear the console after each encounter for better readability (TODO: make this cross-platform compatible)
                player.show_status()
    else:
        print(f"\nFarewell, {player.name}. The pointless quest awaits... when you're ready.")


if __name__ == "__main__":
    main()
