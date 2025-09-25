from pyscript import document

# dictionary with item names as keys and the price as values
menu = {
    "Postcard": 25,
    "Poster": 120,
    "Totebag": 200,
    "Mug": 150,
    "Notebook": 80
}

# function to take note of the order made -- triggered when the order btn is clicked
# 'event=None'-- so it works as an event handler for button clicks
def process_order(event=None):
    name = document.getElementById("cust_name").value
    address = document.getElementById("cust_address").value
    contact = document.getElementById("cust_contact").value

    # makes list of ordered items that the user checks
    # for each item in the shop, check if the corresponding checkbox in the HTML is checked
    # format selected items as "item name – ₱price"
    ordered_items = [
        f"{item} – ₱{price}" 
        for item, price in menu.items() 
        if document.getElementById(item.lower().replace(" ", "")).checked
    ]

    # calculates total price by summing up the prices of all selected items
    # split the "item name – ₱price" string to separate the item name so it can check its price in the shop
    total = sum(menu[item.split(" – ")[0]] for item in ordered_items)

    # if no items were selected, display a warning message
    if not ordered_items:
        items_html = '<span style="color:red">No items selected!</span>'
    else:
        # create an html list of all ordered items
        items_html = "<ul>" +"".join(f"<li>{item}</li>" for item in ordered_items) + "</ul>"

    # create an html string that summarizes the ordered items
    # customer name, address, contact, ordered items, and total price
    summary_html = f"""
    <h4><i><b>Your Order Summary</b></i></h4>
    <p>Order is addressed to <b>{name}</b></p>
    <p>Order will be delivered at <b>{address}</b></p>
    <p>Summertime Museums will call you at <b>{contact}</b></p>
    <p>You bought <br><b>{items_html}</b></p>
    <h5>And your total is <b>₱{total}</b></h5>
    """
    # Insert the order summary html into the html element with id 'order_summary' so it loads with html styling :)
    document.getElementById("order_summary").innerHTML = summary_html

