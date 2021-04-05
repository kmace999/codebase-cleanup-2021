
# TODO: import some code
#using code from class
from app.shopping import format_usd

# TODO: test the code

def test_format_usd():
    #result = format_usd(1999.99)
    assert format_usd(1999.99) == "$1,999.99"


#def test_find_product():
#    assert find_product("DONE") == None 
