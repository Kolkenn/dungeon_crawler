import subprocess
import sys

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

    # Validation loop to confirm player is ready to enter the dungeon, with input validation
    while True:
        # choice = input("Are you ready to enter the dungeon? Y/N : ").strip().upper()
        choice = "Y" # TODO: remove this hardcoding after testing
        match choice:
            case "Y":
                # The player is ready. Break the validation loop to proceed to the game loop.
                break
            case "N":
                print(f"\nFarewell, {player.name}. The pointless quest awaits... when you're ready.")
                sys.exit(1) # Exit the program with a non-zero status to indicate it was intentional but not a successful start.
            case _:
                # Invalid input. The loop continues and prompts the user again.
                print("That wasn't an option you cheeky dog. Please enter Y or N.")

    # Main Loop: runs until player dies, completes the dungeon, or flees (TODO)
    player.show_status()
    print("\nEntering the dungeon...")
    while player.is_alive() and not dungeon.is_complete() and not player.fled():
        dungeon.next_encounter(player)

        if dungeon.is_complete() or player.fled():
            break

        if player.is_alive() and not player.fled():
            # subprocess.run("cls",shell=True) # Clear the console after each encounter for better readability (TODO: make this cross-platform compatible)
            player.show_status()

    # 3. Post-Game Logic
    if not player.is_alive():
        print(f"\nAlas, {player.name} has met their demise in the depths of the dungeon. Better luck next time!")
    elif dungeon.is_complete():
        print(f"\nCongratulations, {player.name}! You have successfully completed the dungeon and emerged victorious! Your name will be remembered by no one as the hero who accomplished nothing of note, but hey, you did it!")
    elif player.fled():
        print(f"\n{player.name} has fled the dungeon. Sometimes discretion is the better part of valor, but the quest remains incomplete. Maybe next time!")

    sys.exit(0) # Exit the program with a zero status to indicate successful completion of the game loop, regardless of the outcome.


if __name__ == "__main__":
    main()
