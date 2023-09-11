#!/usr/bin/python3
""" Rock paper scissors """


from random import randint
from rps import rock_paper

choice = ["Rock", "Paper", "Scissors"]
username = "Anon"

while True:
    """A loop that prompts a user to make a choice"""

    # Receive the users name and choice
    username = input("Please enter your name ")
    try:
        select = int(input("Rock[1], Paper[2], Scissors[3]: "))
        rand = randint(0, 2)
        select = choice[select - 1]
        compChoice = choice[rand]

        # Call the RPS logic and assign the result to result variable
        result = rock_paper(select, compChoice, username)
        print(result)
        print(":)")
        decision = input("Would you like to play again? [yes/no]:  ")
        if decision == "yes" or decision == "Yes":
            pass
        elif decision == "No" or decision == "no":
            break
        else:
            print("You entered an incorrect option :)")
            pass
    except Exception:
        print("Please enter a valid number")
