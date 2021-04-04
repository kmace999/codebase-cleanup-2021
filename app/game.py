
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
    if u==c:
        winner = None

    elif u=="rock":
        if c == "paper":
            winner = c
        elif c== "scissors":
            winner = u

    elif u=="paper":
        if c == "scissors":
            winner = c
        elif c == "rock":
            winner = u

    elif u =="scissors":
        if c == "rock":
            winner = c
        elif u == "paper":
            winner = u

winner = determine_winner(u,c)
if winner ==c:
    print("The computer wins")
elif winner == u:
    print("The user wins")
elif winner == None:
    print("There's a tie!")
