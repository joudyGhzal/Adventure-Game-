import time
import random
import os

# List of characters in the game
random_characters = [
    "wicked fairie", "troll",
    "dragon", "pirate", "Dracula", "gorgon"
]

# Randomly select one character
characters = random.choice(random_characters)
score = 0  # Initializes player score
max_turns = 4  # Maximum turns in the game
winning_score = 25  # Score required to win
wand = False  # Tracks whether player has obtained a better wand
turn_count = 1  # Keeps track of turn number across games
colors = ["blue", "green", "red", "purple", "orange"]

# Choose a random color for the magic wand
wand_color = random.choice(colors)


# Function to print a message and introduce a delay for better game pacing
def print_pause(message):
    print(message)
    time.sleep(2)


# Function to introduce the player to the game world
def intro():
    print_pause(
        "You find yourself standing in an open field, filled with "
        "grass and yellow wildflowers."
    )
    print_pause(
        f"Rumor has it that a {characters} is somewhere around here, and has "
        "been terrifying the nearby village"
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) "
        "rusty old magic wand....."
    )
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


# Function to validate if the player wants to play again
def y_or_n():
    while True:
        choose = input("Would you like to play again? (y/n)\n").strip().lower()
        while choose not in ["y", "n"]:
            choose = input(
                "Would you like to play again? (y/n)\n"
            ).strip().lower()
        return choose


# Function of choices of the game (cave or home)
def selection():
    while True:
        choice = input("(please enter 1 or 2)\n")
        while choice != "1" and choice != "2":
            choice = input("(please enter 1 or 2)\n")
        return choice


# Function of house choice
def house():
    global wand, score
    score += 5
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a "
        f"{characters}."
    )
    print_pause(f"Eep! This is the {characters}'s house!")
    print_pause(f"The {characters} finds you!")
    if not wand:
        print_pause(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny, rusty old magic wand."
        )
    else:
        print_pause(f"you are now facing the {characters}.")
    print_pause(f"Your score now is {score}")
    print_pause("Would you like to (1) cast a spell or (2) run away?")
    print_pause("What would you like to do?\n")


# Function of cave choice
def cave():
    global wand, score
    score += 10
    print_pause("You peer cautiously into the cave")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause(f"You have found the magical {wand_color} Wand of Ogoroth!")
    print_pause(
        "You discard your rusty old magic wand and take the "
        f"{wand_color} Wand of Ogoroth with you.."
    )
    print_pause("You walk back out to the field.")
    print_pause(f"Your score now is {score}")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n")
    wand = True  # Player now has the better wand


# Function of cave again choice
def cave_again():
    print_pause("You peer cautiously into the cave.")
    print_pause(
        "You've been here before, and gotten all the good stuff. "
        "It's just an empty cave now."
    )
    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n")


# Function for defeating the enemy with the magical wand
def success():
    global score
    score += 10
    print_pause(f"You cast the spell and the {characters} is defeated.")
    print_pause(
        f"As the {characters} moves to cast a spell, you raise your"
        f" new {wand_color} Wand of Ogoroth."
    )
    print_pause(
        f"The {wand_color} Wand of Ogoroth shines brightly in your hand as "
        "you brace yourself for the spell."
    )
    print_pause(
        f"But the {characters} takes one look at your shiny new "
        f"{wand_color} wand and runs away!"
    )
    print_pause(
        f"You have rid the town of the {characters}. You are victorious!"
    )
    print_pause(f"Your score now is {score}")


# Function for failing due to a weak wand
def failed():
    global score
    print_pause("You do your best...")
    print_pause(
        f"But your rusty old magic wand is no match for the {characters}."
    )
    print_pause("You have been turned into a frog!")
    score = 0
    print_pause(f"Your score now is {score}")


# Function for running away from the enemy encounter
def run_away():
    print_pause(
        "You run back into the field. Luckily, you don't seem to have been "
        "followed."
    )
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


# Function for handling house-related choices
def house_case():
    global wand
    house()
    choice = selection()
    if choice == "1":
        if wand:
            success()
        else:
            failed()
    else:
        run_away()
        next_choice = selection()
        if next_choice == "1":
            house_case()
        elif next_choice == "2":
            cave_case()


# Function for handling cave-related choices
def cave_case():
    global wand
    if not wand:
        cave()
    else:
        cave_again()
    choice = selection()
    if choice == "1":
        house_case()
    elif choice == "2":
        cave_again()
        next_choice = selection()
        if next_choice == "1":
            house_case()
        elif next_choice == "2":
            cave_case()


# Function to check if the player wants to play again
def play_again():
    global turn_count
    choose = y_or_n()
    if choose == "n":
        return
    elif choose == "y":
        turn_count += 1
        play_adventure_game()


# first riddle functions
def riddle_1():
    global score
    while True:
        answer = input(
            "I don't have lungs, but I need air to live. What am I?\n"
        ).strip().lower()
        if answer == "fire":
            print_pause("Amazing")
            score += 2
            break
        else:
            print_pause("Wrong answer, better luck next time.")
            break


# second riddle functions
def riddle_2():
    global score
    while True:
        answer = input(
            "I have a face and two hands, but no arms or legs. What am I?\n"
        ).strip().lower()
        if answer == "clock":
            print_pause("Amazing")
            score += 2
            break
        else:
            print_pause("Wrong answer, better luck next time.")
            break


# third riddle functions
def riddle_3():
    global score
    while True:
        answer = input(
            "I have a neck but no head, what am I?\n"
            ).strip().lower()
        if answer == "bottle":
            print_pause("Amazing")
            score += 2
            break
        else:
            print_pause("Wrong answer, better luck next time.")
            break


# fourth riddle functions
def riddle_4():
    global score
    while True:
        answer = input(
            "I'm tall when I'm young, and short when I'm old. What am I?\n"
        ).strip().lower()
        if answer == "candle":
            print_pause("Amazing")
            score += 2
            break
        else:
            print_pause("Wrong answer, better luck next time.")
            break


random_riddle = [riddle_1, riddle_2, riddle_3, riddle_4]
selected_riddle = random.choice(random_riddle)


# Main function to run the game
def play_adventure_game():
    global characters, wand, score, turn_count, wand_color
    characters = random.choice(random_characters)
    selected_riddle = random.choice(random_riddle)
    wand_color = random.choice(colors)
    wand = False
    score = 0
    os.system("clear")
    print(f"\nStarting Turn {turn_count}")
    print("~" * 50)
    print("\n")
    intro()
    choice = selection()
    if choice == "1":
        house_case()
    elif choice == "2":
        cave_case()
    print_pause("\nNow there is a riddle\n")
    selected_riddle()
    print_pause(f"Your score is {score}")
    if score >= winning_score:
        print("~" * 50)
        print_pause(f"Game over! You win with {score} points.")
        print("~" * 50)
    else:
        print("~" * 50)
        print_pause(f"Game over! You lose with {score} points.")
        print("~" * 50)
    if turn_count == max_turns:
        print_pause("You reached the maximum number of turns")
        return
    play_again()


# Start the game
if __name__ == "__main__":
    play_adventure_game()
