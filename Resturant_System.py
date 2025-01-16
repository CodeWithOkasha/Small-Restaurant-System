 
                                                             #My Mini Project Resturant System

# Menu of Restaurant
menu = {
    "Pizza": 1000,
    "Burger": 150,
    "Pasta": 250,
    "Shwarma": 200,
    "Rice":450,
    "Roll Pratha": 350
}

print("Welcome to Savour")
print("\n")
print("MENU LIST")
print("-" * 20)

# Display the menu
for dish, price in menu.items():
    print(f"{dish} : {price}")

# Initialize total order
total_order = 0

# Take first order
item_1 = input("\nEnter the item which you want to order: ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been ordered.")
else:
    print(f"Your ordered item {item_1} is not available.")
    

# Ask if the user wants to order another item
another_item = input("\nDo you want to order another item? (Yes/No): ")
if another_item== "Yes":
    item_2 = input("Enter another item you want to order: ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Your next item {item_2} has been ordered.")
    else:
        print(f"Your ordered item {item_2} is not available.")
elif another_items== "No":
    print("No additional items were ordered.")

# Display total bill
print("\nYour total bill is:", total_order)











    
























