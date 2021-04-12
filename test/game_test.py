
# TODO: import some code
from app.game import determine_winner
# TODO: test the code

def test_present_the_winner():
    assert determine_winner("rock","rock") == None
    assert determine_winner("rock","paper") == "paper"
    assert determine_winner("rock","scissors") == "rock"

    assert determine_winner("scissors","scissors") == None
    assert determine_winner("scissors","rock") == "rock"
    assert determine_winner("scissors","paper") == "scissors"

    assert determine_winner("paper","paper") == None
    assert determine_winner("paper","scissors") == "scissors"
    assert determine_winner("paper","rock") == "paper"
#test driven development
#write test first
#write function after so it passes the test
#make sure to add a docstring to the function :)
