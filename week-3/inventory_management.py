inventory = {
    "Apple": [50.0, 60, "Fruits"],
    "Banana": [10.0, 30, "Fruits"],
    "Milk": [40.0, 20, "Dairy"],
    "Cheese": [120.0, 10, "Dairy"],
    "Soap": [30.0, 80, "Toiletries"],
    "Laptop": [999.99, 30, "Electronics"],
    "Shirt": [19.99, 60, "Clothing"],
    "Phone": [499.99, 45, "Electronics"]
}

categories = set()

item_name = input("Enter item name: ")

if item_name not in inventory:
    print("Error: Item not found in inventory")
else:
    selected_category = inventory[item_name][2]
    total_value = 0.0

    for item, details in inventory.items():
        price, quantity, category = details
        categories.add(category)

        if category == selected_category:
            value = price * quantity
            if quantity > 50:
                value *= 0.9
            total_value += value

    output = (total_value, categories)
    print(output)
