import os
from datetime import datetime
from pandas import read_csv

#function based on in-class example
def format_usd(my_price):
    """
    Formats a number as USD with dollar sign, two decimals, and thousands separator

    Params my_price is a number (int or float) that we want to format_usd

    Examples: format_usd(19.99)
    """
    return f"${my_price:,.2f}"


def find_product(prodid,allprods):
    """
    Finds product from local products csv file and adds product to a selected_products list

    Params: prodid (str) like "8", allprods (list of dict) each dict should have "id", "name", "department", "aisle", and "price" attributes

    """
    matching_products = [p for p in allprods if str(p["id"])==str(prodid)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None
    # matching_products = [p for p in products if str(p["id"]) == str(prod)]
    # if any(matching_products):
    #     founditem = matching_products[0]
    #     selected_products.append(founditem)
    #     product_check = founditem["name"]
    # else:
    #     print("OOPS, Couldn't find that product. Please try again.")



products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
products_df = read_csv(products_filepath)
products = products_df.to_dict("records")
#PREVENT ALL THE APP CODE FROM BEING IMPORTED
#BUT STILL BE ABLE TO RUN IT FROM THE COMMAND LINE LIKE THIS
if __name__ == "__main__":
    # READ INVENTORY OF PRODUCTS




    # CAPTURE PRODUCT SELECTIONS

    selected_products = []
    filling_cart = True
    while filling_cart:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            filling_cart = False
        else:
            matching_product = find_product(selected_id,products)
            if matching_product != None:
                selected_products.append(matching_product)
            else:
                print("OOPS, Couldn't find that product. Please try again.")




    checkout_at = datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])

    # PRINT RECEIPT


    formatted_selected_products = []
    for p in selected_products:
        chosenitem = ("SELECTED PRODUCT: " + p["name"] + "   " + '${:.2f}'.format(p["price"]))
        formatted_selected_products.append(chosenitem)

    receipt = [["---------",
    "CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")),
    "---------"],
    formatted_selected_products,
    ["---------",
    f"SUBTOTAL: {format_usd(subtotal)}",
    f"TAX: {format_usd(subtotal * 0.0875)}",
    f"TOTAL: {format_usd((subtotal * 0.0875) + subtotal)}",
    "---------",
    "THANK YOU! PLEASE COME AGAIN SOON!",
    "---------"
    ]]

    for line in receipt:

        for anotherline in line:
            print(anotherline)

    # WRITE RECEIPT TO FILE

    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        for line in receipt:
            for anotherline in line:
                receipt_file.write(f"\n {anotherline}")
