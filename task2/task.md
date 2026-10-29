Problem Statement
The aim of this project is to develop a Progressive Electricity Billing System using Python to calculate household electricity bills based on multiple consumption slabs. The system accepts electricity consumption in units (kWh) and calculates charges for each slab progressively.

The program includes fixed charges, surcharges, and rebates to determine the final payable amount. It also records electricity bills for several months, compares monthly bills, and identifies unusual increases in electricity consumption or billing amounts. This system helps households monitor electricity expenses and understand changes in their monthly bills.

2. Algorithm
Start the program.

Define the electricity tariff rates for different consumption slabs.

Define the fixed charge, surcharge percentage, and rebate percentage.

Input the number of months for which bills must be calculated.

For each month:

Enter the month name and electricity consumption in units.

Calculate the energy charges using progressive slabs.

Add fixed charges to obtain the subtotal.

Calculate the surcharge on the subtotal.

Calculate the eligible rebate.

Calculate the final bill amount.

Store the consumption and bill amount.

Compare each month's bill with the previous month's bill.

Calculate the percentage increase or decrease in the bill.

If the increase exceeds a specified threshold, identify the bill as an unusual increase.

Display the monthly bill details and comparison report.

Stop the program.

Progressive slab calculation
For example, assume the following illustrative tariff rates:

Consumption slab

Rate per unit

First 100 units

₹2.00

Next 100 units

₹3.00

Next 300 units

₹5.00

Above 500 units

₹7.00

For a consumption of 250 units:

First 100 units: 
100
×
₹
2
=
₹
200
100×₹2=₹200

Next 100 units: 
100
×
₹
3
=
₹
300
100×₹3=₹300

Remaining 50 units: 
50
×
₹
5
=
₹
250
50×₹5=₹250

Total energy charge = ₹750.

These are example rates for the project, not an official electricity tariff.

3. Mermaid Flowchart

mermaid

flowchart TD
    A([Start]) --> B[Define Slab Rates and Billing Rules]
    B --> C[/Enter Number of Months/]
    C --> D[/Enter Month and Units Consumed/]
    D --> E[Calculate Progressive Slab Charges]
    E --> F[Add Fixed Charges]
    F --> G[Calculate Surcharge and Rebate]
    G --> H[Calculate Final Bill]
    H --> I[Store Monthly Units and Bill]
    I --> J{More Months?}
    J -- Yes --> D
    J -- No --> K[Compare Consecutive Monthly Bills]
    K --> L[Calculate Percentage Changes]
    L --> M{Increase Above Threshold?}
    M -- Yes --> N[Flag Unusual Increase]
    M -- No --> O[Mark as Normal Change]
    N --> P[Display Monthly Bills and Report]
    O --> P
    P --> Q([Stop])

    style A fill:#d4edda,stroke:#287a43
    style Q fill:#d4edda,stroke:#287a43
    style N fill:#fff3cd,stroke:#b8860b
4. Input
The program accepts the following inputs:

Input

Example

Number of months

3

Month 1

January

January consumption

150 units

Month 2

February

February consumption

180 units

Month 3

March

March consumption

280 units

Fixed charge per month

₹50

Surcharge rate

5%

Rebate rate

2%

Unusual increase threshold

20%

5. Expected Output
The following is an illustrative output using the sample tariff and billing inputs above.

Month

Units

Energy charge

Final bill

January

150

₹350.00

₹411.60

February

180

₹440.00

₹505.80

March

280

₹900.00

₹1,012.80

The final bill assumes the fixed charge is added to energy charges, a 5% surcharge is applied to that subtotal, and a 2% rebate is deducted from the same subtotal.

Monthly comparison:

February increased by approximately 22.89% compared with January — unusual increase.

March increased by approximately 100.24% compared with February — unusual increase.
