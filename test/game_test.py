
# TODO: import some code
from app.game import determine_winner
# TODO: test the code

def test_present_the_winner():
    assert determine_winner("rock","rock") == "It's a tie!"
    assert determine_winner("rock","paper") == "The computer wins"
    assert determine_winner("rock","scissors") == "The user wins"
    assert determine_winner("scissors","scissors") == "It's a tie!"
    assert determine_winner("scissors","rock") == "The computer wins"
    assert determine_winner("scissors","paper") == "The user wins"
    assert determine_winner("paper","paper") == "It's a tie!"
    assert determine_winner("paper","rock") == "The user wins"
    assert determine_winner("paper","scissors") == "The computer wins"
#test driven development
#write test first
#write function after so it passes the test
#make sure to add a docstring to the function :)
