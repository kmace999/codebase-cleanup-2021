
# TODO: import some code
from app.game import determine_winner
# TODO: test the code

def test_present_the_winner():
    assert determine_winner("rock","rock") == None
    assert determine_winner("rock","paper") == c
    assert determine_winner("rock","scissors") == u
    assert determine_winner("scissors","scissors") == None
    assert determine_winner("scissors","rock") == c
    assert determine_winner("scissors","paper") == u
    assert determine_winner("paper","paper") == None
    assert determine_winner("paper","rock") == u
    assert determine_winner("paper","scissors") == c
#test driven development
#write test first
#write function after so it passes the test
#make sure to add a docstring to the function :)
