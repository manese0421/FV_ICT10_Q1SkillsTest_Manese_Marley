from pyscript import document

menu = {
    "Postcard": 25,
    "Poster": 120,
    "Totebag": 200,
    "Mug": 150,
    "Notebook": 80
}

def process_order(event=None):
    name = document.getElementById("cust_name").value
    address = document.getElementById("cust_address").value
    contact = document.getElementById("cust_contact").value

    ordered_items = [
        f"{item} – ₱{price}" 
        for item, price in menu.items() 
        if document.getElementById(item.lower().replace(" ", "")).checked
    ]
    total = sum(menu[item.split(" – ")[0]] for item in ordered_items)

    if not ordered_items:
        items_html = '<span style="color:red">No items selected!</span>'
    else:
        items_html = "<ul>" +"".join(f"<li>{item}</li>" for item in ordered_items) + "</ul>"

    summary_html = f"""
    <h4><i><b>Your Order Summary</b></i></h4>
    <p>Order is addressed to <b>{name}</b></p>
    <p>Order will be delivered at <b>{address}</b></p>
    <p>Summertime Museums will call you at <b>{contact}</b></p>
    <p>You bought <br><b>{items_html}</b></p>
    <h5>And your total is <b>₱{total}</b></h5>
    """

    document.getElementById("order_summary").innerHTML = summary_html
