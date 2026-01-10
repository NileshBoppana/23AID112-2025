shopping_list = []

while True:
    action = input("What do you want to do? (add/remove/show/quit): ").lower()

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the shopping list.")
    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the shopping list.")
        else:
            print(f"{item} not found in the shopping list.")
    elif action == "show":
        print("Current shopping list:", shopping_list)
    elif action == "quit":
        print("Exiting the shopping list manager.")
        break
    else:
        print("Invalid action. Please choose add, remove, show, or quit.")
