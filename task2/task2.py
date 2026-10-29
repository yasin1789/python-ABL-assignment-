
def calculate_bill(units, fixed_charge, surcharge_rate, rebate):
    """
    Calculate electricity bill using progressive slab rates.
    Slabs:
      0-50 units:   Rs. 1.50/unit
      51-150 units: Rs. 3.00/unit
      151-300 units: Rs. 5.00/unit
      Above 300:    Rs. 7.00/unit
    """

    energy_charge = 0

    # Slab 1: First 50 units
    slab1 = min(units, 50)
    energy_charge += slab1 * 1.50

    # Slab 2: Next 100 units
    slab2 = min(max(units - 50, 0), 100)
    energy_charge += slab2 * 3.00

    # Slab 3: Next 150 units
    slab3 = min(max(units - 150, 0), 150)
    energy_charge += slab3 * 5.00

    # Slab 4: Above 300 units
    slab4 = max(units - 300, 0)
    energy_charge += slab4 * 7.00

    # Calculate surcharge on energy charges
    surcharge = energy_charge * surcharge_rate / 100

    # Calculate total bill before rebate
    total = energy_charge + fixed_charge + surcharge

    # Apply rebate without allowing a negative bill
    total = max(0, total - rebate)

    return energy_charge, surcharge, total


def main():
    months = []
    num_months = int(input("Enter number of months: "))

    for i in range(num_months):
        print(f"\nMonth {i + 1}")

        month = input("Enter month name: ")
        units = float(input("Enter electricity units consumed: "))
        fixed_charge = float(input("Enter fixed charge (Rs.): "))
        surcharge_rate = float(input("Enter surcharge rate (%): "))
        rebate = float(input("Enter rebate (Rs.): "))

        energy, surcharge, bill = calculate_bill(
            units, fixed_charge, surcharge_rate, rebate
        )

        print(f"Energy Charges : Rs. {energy:.2f}")
        print(f"Surcharge      : Rs. {surcharge:.2f}")
        print(f"Total Bill     : Rs. {bill:.2f}")

        months.append({
            "month": month,
            "units": units,
            "bill": bill
        })

    # Compare monthly bills
    print("\n========== MONTHLY BILL COMPARISON ==========")

    for i, record in enumerate(months):
        print(
            f"{record['month']}: "
            f"{record['units']:.0f} units, "
            f"Bill = Rs. {record['bill']:.2f}"
        )

        if i > 0:
            previous_bill = months[i - 1]["bill"]
            current_bill = record["bill"]

            if previous_bill > 0:
                change = (
                    (current_bill - previous_bill)
                    / previous_bill
                ) * 100

                print(f"Bill change: {change:+.2f}%")

                if change > 25:
                    print("WARNING: Unusual increase in electricity bill!")
                elif change < -25:
                    print("Notice: Electricity bill decreased significantly.")

    print("\n========== ANALYSIS COMPLETE ==========")


if __name__ == "__main__":
    main()


   
