
from random import choice

#
# USER SELECTION
# incorporating code from class demonstrations
VALID_OPTIONS = ["rock","paper","scissors"]
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#
def determine_winner(u,c):
    """
    Determines winner of rock, paper, scissors game.

    Params u is the user's move validated from ["rock","paper","scissors"]
    and c is the computer's move randomly generated from ["rock","paper","scissors"]

    Examples: determine_winner("rock","paper")
    """
    if user==c:
        print("It's a tie!")

    elif u=="rock":
        if c == "paper":
            print("The computer wins")
        elif c== "scissors":
            print("The user wins")

    elif u=="paper":
        if c == "scissors":
            print("The computer wins")
        elif c == "rock":
            print("The user wins")

    elif u =="scissors":
        if c == "rock":
            print("The computer wins")
        elif u == "paper":
            print("The user wins")

determine_winner(u,c)
