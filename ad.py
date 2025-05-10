     
import time
wand=False
def print_pause(massege):
    print(massege)
    time.sleep(2)

def intro():   
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) rusty old magic wand.....")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")

print("\n")
def selection():
    while True:
        choice=input("(please enter 1 or 2)\n") 
        
        while (choice!="1"and choice!="2") :
            choice=input("(please enter 1 or 2)\n") 
        
        return choice

def house():
    global wand
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a dragon.")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon finds you!")
    if wand!=True:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
    else:
        print_pause("you are now facing the dragon.")
    print_pause("Would you like to (1) cast a spell or (2) run away?\n")

def cave():
    global wand
    print_pause("You peer cautiously into the cave")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Wand of Ogoroth!")
    print_pause("You discard your rusty old magic wand and take the Wand of Ogoroth with you..")
    print_pause("You walk back out to the field.") 
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    wand=True

def cave_again(): 
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
 
def success():
    print_pause("You cast the spell and the dragon is defeated.")
    print_pause("As the gorgon moves to cast a spell, you raise your new Wand of Ogoroth.")
    print_pause("The Wand of Ogoroth shines brightly in your hand as you brace yourself for the spell.")
    print_pause("But the gorgon takes one look at your shiny new wand and runs away!")
    print_pause("You have rid the town of the gorgon. You are victorious!")
    print_pause("Would you like to play again? (y/n)")

def failed():

    print_pause("You do your best...")
    print_pause("but your rusty old magic wand is no match for the troll.")
    print_pause("You have been turned into a frog!")
    print_pause("Would you like to play again? (y/n)")

def run_away():

    print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

def house_case():
    house()
    choice =selection()
    if choice=="1":
        if wand==True:
            success()
        else:
            failed()
    else :
        run_away()
        choice =selection()
        if choice=="1":
            house_case()
        elif choice=="2":
            cave_case()

def cave_case():
    if wand==False:
        cave()
    else:
        cave_again()

    choice =selection()
    if choice=="1":
        house_case()
    elif choice=="2":
        cave_again()
        choice =selection()
        if choice=="1":
            house_case()
        elif choice=="2":
            cave_case()



def play_adventure_game():
    intro()
    choice =selection()
    if choice=="1":
        house_case()
    elif choice=="2":
        cave_case()

play_adventure_game()
