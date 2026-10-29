
# Progressive Electricity Billing System

# Electricity tariff rates (illustrative)
SLAB1_LIMIT = 100
SLAB2_LIMIT = 200
SLAB3_LIMIT = 500

RATE1 = 2.00
RATE2 = 3.00
RATE3 = 5.00
RATE4 = 7.00

FIXED_CHARGE = 50.00
SURCHARGE_RATE = 5.00
REBATE_RATE = 2.00
INCREASE_THRESHOLD = 20.00


# Function to calculate progressive energy charges
def calculate_energy_charge(units):
    if units <= 0:
        return 0.0

    if units <= SLAB1_LIMIT:
        charge = units * RATE1

    elif units <= SLAB2_LIMIT:
        charge = (SLAB1_LIMIT * RATE1) + (
            (units - SLAB1_LIMIT) * RATE2
        )

    elif units <= SLAB3_LIMIT:
        charge = (
            SLAB1_LIMIT * RATE1
            + (SLAB2_LIMIT - SLAB1_LIMIT) * RATE2
            + (units - SLAB2_LIMIT) * RATE3
        )

    else:
        charge = (
            SLAB1_LIMIT * RATE1
            + (SLAB2_LIMIT - SLAB1_LIMIT) * RATE2
            + (SLAB3_LIMIT - SLAB2_LIMIT) * RATE3
            + (units - SLAB3_LIMIT) * RATE4
        )

    return charge


# Function to calculate the final bill
def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)

    subtotal = energy_charge + FIXED_CHARGE
    surcharge = subtotal * SURCHARGE_RATE / 100
    rebate = subtotal * REBATE_RATE / 100

    total_bill = subtotal + surcharge - rebate

    return energy_charge, surcharge, rebate, total_bill


# Main program
print("=" * 55)
print("       PROGRESSIVE ELECTRICITY BILLING SYSTEM")
print("=" * 55)

months = int(input("Enter number of months: "))

if months <= 0:
    print("Please enter a valid number of months.")

else:
    records = []

    for i in range(months):
        print(f"\nEnter details for Month {i + 1}")

        month = input("Enter month name: ")
        units = float(input("Enter electricity units consumed: "))

        if units < 0:
            print("Units cannot be negative. Please try again.")
            continue

        energy, surcharge, rebate, total = calculate_bill(units)

        records.append({
            "month": month,
            "units": units,
            "energy": energy,
            "surcharge": surcharge,
            "rebate": rebate,
            "total": total
        })

        print("\n--- Monthly Bill ---")
        print(f"Month           : {month}")
        print(f"Units Consumed  : {units:.2f}")
        print(f"Energy Charges  : Rs. {energy:.2f}")
        print(f"Fixed Charges   : Rs. {FIXED_CHARGE:.2f}")
        print(f"Surcharge       : Rs. {surcharge:.2f}")
        print(f"Rebate          : Rs. {rebate:.2f}")
        print(f"Total Bill      : Rs. {total:.2f}")

    # Monthly comparison report
    print("\n" + "=" * 65)
    print("              MONTHLY BILL COMPARISON")
    print("=" * 65)

    print(f"{'Month':<15}{'Units':>10}{'Bill (Rs.)':>15}{'Change':>15}")

    for i, record in enumerate(records):
        if i == 0:
            change_text = "N/A"
        else:
            previous = records[i - 1]["total"]
            current = record["total"]

            if previous > 0:
                change = ((current - previous) / previous) * 100
                change_text = f"{change:+.2f}%"

                if change > INCREASE_THRESHOLD:
                    change_text += " ALERT"
            elif current > 0:
                change_text = "New bill ALERT"
            else:
                change_text = "0.00%"

        print(
            f"{record['month']:<15}"
            f"{record['units']:>10.2f}"
            f"{record['total']:>15.2f}"
            f"{change_text:>15}"
        )

    print("=" * 65)
    print("Note: ALERT indicates a bill increase above 20%.")
    print("Thank you for using the billing system!")

