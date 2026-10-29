
# Retail Billing with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

# Input customer details
customer_name = input("Enter customer name: ")

# Input item details
n = int(input("Enter number of items: "))

subtotal = 0
items = []

for i in range(n):
    print(f"\nItem {i + 1}")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    subtotal += amount

    items.append((name, price, quantity, amount))

# Apply discount rules
discount = 0

# Rule 1: 10% discount for bills above 5000
if subtotal > 5000:
    discount += subtotal * 0.10

# Rule 2: Additional 5% discount for bills above 10000
if subtotal > 10000:
    discount += subtotal * 0.05

# Rule 3: Additional 2% discount for bills above 20000
if subtotal > 20000:
    discount += subtotal * 0.02

# Rule 4: Maximum discount limited to 20%
discount = min(discount, subtotal * 0.20)

# Calculate final bill
final_amount = subtotal - discount

# Display bill
print("\n========== CUSTOMER BILL ==========")
print("Customer Name:", customer_name)
print("-----------------------------------")
print(f"{'Item':<15}{'Price':>8}{'Qty':>6}{'Amount':>10}")

for name, price, quantity, amount in items:
    print(f"{name:<15}{price:>8.2f}{quantity:>6}{amount:>10.2f}")

print("-----------------------------------")
print(f"Subtotal:       Rs. {subtotal:.2f}")
print(f"Discount:       Rs. {discount:.2f}")
print(f"Final Amount:   Rs. {final_amount:.2f}")
print("===================================")
print("Thank you for shopping!")

