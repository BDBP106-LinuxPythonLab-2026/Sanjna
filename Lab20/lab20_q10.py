# inventory and billing system

inventory = {
"pen": (10.0, 50), # (price, quantity in stock)
"notebook": (45.0, 20),
"eraser": (5.0, 100),
"marker": (30.0, 15),
}

cart = {}

while True:
# entry processing
    entry= input("Enter item and quantity or 'done': ").strip().lower()
    if entry == "done": break

    order = entry.split()
    if len(order) != 2:
        print("Enter: item quantity ")
        continue

#checking entry items
    item, qty = order
    if item not in inventory:
        print(f"Sorry, '{item}' is not available. ")
        continue
    if not qty.isdigit() or int(qty) == 0:
        print("Quantity must be a positive whole number.")
        continue

    quantity = int(qty)
    price, stock = inventory[item]
    if quantity > stock:
        print(f"Insufficient stock. Only {stock} {item}s left.")
        continue
#updating cart
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
#updating inventory
    new_stock = stock - quantity
    inventory[item] = (price, new_stock)
    print(f"Added {quantity} {item}s to cart.")

#creating receipt

print()
if not cart: print("No item purchased.")
else:
    print("Receipt")
    print("Item".ljust(12) + "Quantity".rjust(10) + "Price".rjust(10) + "Total".rjust(10))
    print("-" * 37)
    subtotal = 0
    for item, quantity in cart.items():
        price = inventory[item][0]
        item_total = price * quantity
        subtotal += item_total
        print(item.ljust(12) + str(quantity).rjust(10) + f"{price:.2f}".rjust(10) + f"{item_total:.2f}".rjust(10))
    print("-" * 37)
    print("Subtotal".ljust(27) +f"{subtotal:.2f}".rjust(10))
    discount = 0
    if subtotal > 500:
        discount = subtotal * 0.10
        print("Discount Applied!".ljust(30) + f"{subtotal - discount:.2f}".rjust(10))
    print("Total".ljust(27) + f"{subtotal - discount:.2f}".rjust(10))

#updating inventory
print()
print("Updated inventory: ")
for item, (price,stock) in inventory.items():
    check = "LOW STOCK" if stock < 10 else ""
    print(f"{item.ljust(12)}{str(stock).rjust(5)}  {check}")

        




