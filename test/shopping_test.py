
# TODO: import some code
#using code from class
from app.shopping import format_usd

# TODO: test the code

def test_format_usd():
    result = format_usd(1999.99)
    assert result == "$1,999.99"
