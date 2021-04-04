
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
def determine_winner(user,comp):
    """
    Determines winner of rock, paper, scissors game.

    Params user is the user's move validated from ["rock","paper","scissors"]
    and comp is the computer's move randomly generated from ["rock","paper","scissors"]

    Examples: determine_winner("rock","paper")
    """
    if user==comp:
        winner = None

    elif user=="rock":
        if comp == "paper":
            winner = c
        elif comp== "scissors":
            winner = u

    elif user=="paper":
        if comp == "scissors":
            winner = c
        elif comp == "rock":
            winner = u

    elif user =="scissors":
        if comp == "rock":
            winner = c
        elif comp == "paper":
            winner = u

winner = determine_winner(u,c)
if winner ==c:
    print("The computer wins")
elif winner == u:
    print("The user wins")
elif winner == None:
    print("There's a tie!")
