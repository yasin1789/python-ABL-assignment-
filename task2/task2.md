# Problem Statement
The Progressive Electricity Billing System is designed to calculate household electricity bills based on the number of units consumed using a progressive slab tariff system. The program calculates energy charges for each slab, adds fixed charges and surcharges, and deducts applicable rebates to determine the total electricity bill.

The system also stores electricity consumption and bill details for multiple months, compares consecutive monthly bills, calculates the percentage change, and identifies unusual increases or significant decreases in electricity charges. This helps consumers monitor their electricity usage and manage their monthly expenses.

# Algorithm
Start the program.

Define a function to calculate the electricity bill using progressive slab rates:

First 50 units: ₹1.50 per unit.

Next 100 units: ₹3.00 per unit.

Next 150 units: ₹5.00 per unit.

Above 300 units: ₹7.00 per unit.

Input the number of months for which bills must be calculated.

For each month, input:

Month name.

Electricity units consumed.

Fixed charge.

Surcharge percentage.

Rebate amount.

Calculate energy charges for each slab based on the units consumed.

Calculate the surcharge on energy charges.

Add energy charges, fixed charges, and surcharge.

Deduct the rebate to calculate the final bill, ensuring the bill does not become negative.

Display the energy charges, surcharge, and total bill.

Store the month name, units consumed, and total bill.

Compare each month's bill with the previous month's bill.

Calculate the percentage change in the bill.

If the increase is greater than 25%, display an unusual-increase warning.

If the decrease is greater than 25%, display a significant-decrease message.

Display the monthly bill comparison and end the program.

# Mermaid flowchart

``mermaid

flowchart TD
    A([Start]) --> B[/Input number of months/]
    B --> C[Initialize monthly records]
    C --> D[/Input month, units, fixed charge, surcharge and rebate/]
    D --> E[Calculate slab-wise energy charges]
    E --> F[Calculate surcharge]
    F --> G[Add energy charges and fixed charges]
    G --> H[Deduct rebate]
    H --> I[Calculate final bill]
    I --> J[/Display bill details/]
    J --> K[Store month, units and bill]
    K --> L{More months?}
    L -- Yes --> D
    L -- No --> M[Compare consecutive monthly bills]
    M --> N[Calculate percentage change]
    N --> O{Increase greater than 25%?}
    O -- Yes --> P[Display unusual increase warning]
    O -- No --> Q{Decrease greater than 25%?}
    Q -- Yes --> R[Display significant decrease]
    Q -- No --> S[Display normal bill change]
    P --> T[/Display monthly comparison/]
    R --> T
    S --> T
    T --> U([End])
# Input
The program accepts the following inputs from the user.

Input

Description

Example

Number of months

Total months to calculate

3

Month name

Billing month

January

Units consumed

Electricity usage in units

200

Fixed charge

Fixed monthly charge in rupees

75

Surcharge rate

Surcharge percentage

5

Rebate

Discount in rupees

20

Sample input

text
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity units consumed: 150
Enter fixed charge (Rs.): 75
Enter surcharge rate (%): 5
Enter rebate (Rs.): 20

Month 2
Enter month name: February
Enter electricity units consumed: 200
Enter fixed charge (Rs.): 75
Enter surcharge rate (%): 5
Enter rebate (Rs.): 20

Month 3
Enter month name: March
Enter electricity units consumed: 300
Enter fixed charge (Rs.): 75
Enter surcharge rate (%): 5
Enter rebate (Rs.): 20
5. Expected result
The program calculates and displays the electricity bill for each month, including energy charges, surcharge, and final bill. It then compares monthly bills and identifies unusual increases or significant decreases.

For the sample input, the final bills are:

Month

Units

Total bill

January

150

₹396.75

February

200

₹711.25

March

300

₹1,236.25

February shows a significant increase compared with January.

March shows a significant increase compared with February.

Both increases exceed the program's 25% warning threshold.



