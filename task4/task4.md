# Problem Statement
Develop a Python program for a retail billing system that calculates the total purchase amount of a customer and applies multiple discount rules based on the bill amount.

The program should accept the customer's name, the number of items, item names, prices, and quantities. It should calculate the subtotal, apply the applicable discounts, limit the maximum discount to 20% of the subtotal, and display a detailed bill containing the item details, subtotal, discount amount, and final amount payable.

Discount rules
If the subtotal is above ₹5,000, apply a 10% discount.

If the subtotal is above ₹10,000, apply an additional 5% discount.

If the subtotal is above ₹20,000, apply an additional 2% discount.

The total discount must not exceed 20% of the subtotal.

# Algorithm
Start the program.

Read the customer's name.

Read the number of items.

Initialize the subtotal to zero.

For each item:

Read the item name, price, and quantity.

Calculate the item amount as price × quantity.

Add the item amount to the subtotal.

Store the item details.

Initialize the discount to zero.

If the subtotal is greater than ₹5,000, add a 10% discount.

If the subtotal is greater than ₹10,000, add an additional 5% discount.

If the subtotal is greater than ₹20,000, add an additional 2% discount.

Limit the discount to 20% of the subtotal.

Calculate the final amount as subtotal − discount.

Display the customer's details, itemized bill, subtotal, discount, and final amount.

Stop the program.

# Mermaid flowchart

mermaid

flowchart TD
    A([Start]) --> B[/Enter customer name/]
    B --> C[/Enter number of items/]
    C --> D[Initialize subtotal = 0]
    D --> E[/Enter item name, price and quantity/]
    E --> F[Calculate amount = price × quantity]
    F --> G[Add amount to subtotal]
    G --> H{More items?}
    H -- Yes --> E
    H -- No --> I[Initialize discount = 0]
    I --> J{subtotal > 5000?}
    J -- Yes --> K[Add 10% discount]
    J -- No --> L{subtotal > 10000?}
    K --> L
    L -- Yes --> M[Add additional 5% discount]
    L -- No --> N{subtotal > 20000?}
    M --> N
    N -- Yes --> O[Add additional 2% discount]
    N -- No --> P[Limit discount to 20%]
    O --> P
    P --> Q[Calculate final amount]
    Q --> R[/Display detailed bill/]
    R --> S([Stop])
Note: In the flowchart, each discount condition is checked independently, so applicable discounts are cumulative. The maximum discount is capped at 20%.

# Input

text
Enter customer name: Ravi
Enter number of items: 2

Item 1
Enter item name: Shirt
Enter item price: 1500
Enter quantity: 2

Item 2
Enter item name: Shoes
Enter item price: 4000
Enter quantity: 1
5. Expected output

text
========== CUSTOMER BILL ==========

Customer Name: Ravi

Item              Price   Qty    Amount
Shirt           1500.00     2   3000.00
Shoes           4000.00     1   4000.00

Subtotal:       Rs. 7000.00
Discount:       Rs. 700.00
Final Amount:   Rs. 6300.00

Thank you for shopping!
6. Result
The retail billing system successfully calculates the subtotal, applies multiple discount rules, enforces the maximum discount limit, and displays the final amount payable by the customer.



