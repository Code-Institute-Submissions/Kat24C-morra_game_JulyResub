import random


def game_choice():
    """
    Here we are going to ask the user to input a number
    between 1 and 3.
    The computer will randomize a number between 1 and 3.
    Then we will compare the two numbers to see if they
    are the same or different.
    """
    while True: 
        try: 
            user_choice = int(input("Choose a number between 1 and 3: "))
        except ValueError: 
            print("Please enter a valid number")
            user_choice = int(input("Choose a number between 1 and 3: "))
        
        computer_guess = random.randint(1, 3)
        print(f"The computer chose: {computer_guess}\n")
        
        try:
            user_guess = int(input("Guess the computers number 1, 2 or 3: "))
        except ValueError: 
            print("Please enter a valid number")
            user_guess = int(input("Guess the computers number 1, 2, 3: "))
        
        computer_choice = random.randint(1, 3)
        print(f"The computer chose: {computer_choice}\n")