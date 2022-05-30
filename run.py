import random


def game_choice():
    """
    Here we are going to ask the user to input a number
    between 1 and 3.
    The computer will randomize a number between 1 and 3.
    Then we will compare the two numbers to see if they
    are the same or different.
    """
    player_score = 0
    comp_score = 0
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

        if user_guess == computer_choice:
            user_score = user_guess + computer_choice
            print(f"Well done, You got {user_score}")
            player_score = player_score + user_score
            print(f"Your total is {player_score}\n")
        else:
            print("Oh dear, try again you got 0")
            print(f"Your total is {player_score}")

        if user_choice == computer_guess:
            computer_score = user_choice + computer_guess
            print(f"The computer got {computer_score}")
            comp_score = comp_score + computer_score
            print(f"The computer's total is {comp_score}\n")
        else:
            print("The computer got 0")
            print(f"The computer's total is {comp_score}\n")