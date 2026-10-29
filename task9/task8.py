# Smart Canteen Order and Stock Management

# Initial menu and stock
menu = {
    "Idli": {"price": 30, "stock": 20},
    "Dosa": {"price": 50, "stock": 15},
    "Sandwich": {"price": 60, "stock": 10},
    "Juice": {"price": 25, "stock": 12}
}

total_sales = 0

print("===== SMART CANTEEN MANAGEMENT =====")

while True:
    print("\n--- CANTEEN MENU ---")
    print(f"{'Item':<15}{'Price (Rs.)':<15}{'Stock':<10}")

    for item, details in menu.items():
        print(
            f"{item:<15}"
            f"{details['price']:<15}"
            f"{details['stock']:<10}"
        )

    print("\n1. Place Order")
    print("2. View Stock")
    print("3. View Sales")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        item = input("Enter food item: ").strip().title()

        if item not in menu:
            print("Item not available in the menu.")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > menu[item]["stock"]:
            print("Insufficient stock!")
            print("Available quantity:", menu[item]["stock"])
            continue

        price = menu[item]["price"]
        amount = price * quantity

        # Update stock and sales
        menu[item]["stock"] -= quantity
        total_sales += amount

        print("\n--- ORDER CONFIRMED ---")
        print("Item:", item)
        print("Quantity:", quantity)
        print(f"Price per item: Rs. {price:.2f}")
        print(f"Total bill: Rs. {amount:.2f}")
        print("Order placed successfully!")

    elif choice == "2":
        print("\n--- CURRENT STOCK ---")
        for item, details in menu.items():
            print(
                f"{item}: {details['stock']} units available"
            )

    elif choice == "3":
        print(f"\nTotal sales: Rs. {total_sales:.2f}")

    elif choice == "4":
        print("\n===== FINAL REPORT =====")
        print(f"Total sales: Rs. {total_sales:.2f}")
        print("\nRemaining stock:")

        for item, details in menu.items():
            print(f"{item}: {details['stock']}")

        print("Thank you for using Smart Canteen Management!")
        break

    else:
        print("Invalid choice. Please try again.")
