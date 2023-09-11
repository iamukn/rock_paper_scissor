#!/usr/bin/python3
""" Method that validates the RPS game input """


def rock_paper(choice1: str, choice2: str, username: str) -> str:
    """Receives user & comp choice and checks for the winner of the game"""
    # conditions that compares the users choice with that of the computer
    if choice1 == choice2:
        print(f"{username}: {choice1} || Alice: {choice2}")
        return "Woah!! It's a Tie :)"

    elif choice1 == "Rock" and choice2 == "Paper":
        print(f"{username}: {choice1} || Alice: {choice2}")
        return "Alice: Wins!"

    elif choice1 == "Rock" and choice2 == "Scissors":
        print(f"{username}: {choice1} || Alice: {choice2}")
        return f"{username}: Wins!"

    elif choice1 == "Paper" and choice2 == "Rock":
        print(f"{username}: {choice1} || Alice: {choice2}")
        return f"{username}: Wins!"

    elif choice1 == "Paper" and choice2 == "Scissors":
        print(f"{username}: {choice1} || Alice: {choice2}")
        return "Alice: Wins!"
    elif choice1 == "Scissors" and choice2 == "Rock":
        print(f"{username}: {choice1} || Alice: {choice2}")
        return "Alice: Wins!"
    elif choice1 == "Scissors" and choice2 == "Paper":
        print(f"{username}: {choice1} || Alice: {choice2}")
        return f"{username}: Wins!"
