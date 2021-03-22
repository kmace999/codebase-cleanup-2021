
from random import choice

#
# USER SELECTION
#
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

if u==c:
    print("It's a tie!")

if u=="rock":
    if c == "paper":
        print("The computer wins")
    elif c== "scissors":
        print("The user wins")

elif u=="paper":
    if c == "rock":
        print("The computer wins")
    elif c == "scissors":
        print("The user wins")

else:
    if c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
