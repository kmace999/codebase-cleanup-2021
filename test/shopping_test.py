
# TODO: import some code
#using code from class
from app.shopping import format_usd
from app.shopping import find_product

# TODO: test the code

def test_format_usd():
    #result = format_usd(1999.99)
    assert format_usd(1999.99) == "$1,999.99"


def test_find_product():
   assert find_product("DONE") == None
   assert find_product("1") == ["Chocolate Sandwich Cookies"]
   assert find_product("2") == ["All-Seasons Salt"]
   assert find_product("3") == ["Robust Golden Unsweetened Oolong Tea"]
   assert find_product("4") == ["Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce"]
   assert find_product("5") == ["Green Chile Anytime Sauce"]
   assert find_product("6") == ["Dry Nose Oil"]
   assert find_product("7") == ["Pure Coconut Water With Orange"]
   assert find_product("8") == ["Cut Russet Potatoes Steam N' Mash"]
   assert find_product("9") == ["Light Strawberry Blueberry Yogurt"]
   assert find_product("10") == ["Sparkling Orange Juice & Prickly Pear Beverage"]
   assert find_product("11") == ["Peach Mango Juice"]
   assert find_product("12") == ["Chocolate Fudge Layer Cake"]
   assert find_product("13") == ["Saline Nasal Mist"]
   assert find_product("14") == ["Fresh Scent Dishwasher Cleaner"]
   assert find_product("15") == ["Overnight Diapers Size 6"]
   assert find_product("16") == ["Mint Chocolate Flavored Syrup"]
   assert find_product("17") == ["Rendered Duck Fat"]
   assert find_product("18") == ["Pizza for One Suprema  Frozen Pizza"]
   assert find_product("19") == ["Gluten Free Quinoa Three Cheese & Mushroom Blend"]
   assert find_product("20") == ["Pomegranate Cranberry & Aloe Vera Enrich Drink"]
