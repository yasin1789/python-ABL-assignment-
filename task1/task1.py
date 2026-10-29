
# Hospital Billing System

print("=" * 45)
print("         HOSPITAL BILLING SYSTEM")
print("=" * 45)

# Patient details
patient_id = input("Enter Patient ID: ")
patient_name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
doctor_name = input("Enter Doctor Name: ")

# Hospital service charges
consultation = float(input("Enter Consultation Fee: ₹"))
room_charges = float(input("Enter Room Charges: ₹"))
medicine_charges = float(input("Enter Medicine Charges: ₹"))
lab_charges = float(input("Enter Laboratory Charges: ₹"))

# Calculate total
subtotal = (
    consultation
    + room_charges
    + medicine_charges
    + lab_charges
)

discount_percent = float(input("Enter Discount (%): "))
discount = subtotal * discount_percent / 100

total_bill = subtotal - discount

# Print bill receipt
print("\n" + "=" * 45)
print("              HOSPITAL BILL")
print("=" * 45)

print(f"Patient ID       : {patient_id}")
print(f"Patient Name     : {patient_name}")
print(f"Age              : {age}")
print(f"Doctor Name      : {doctor_name}")

print("-" * 45)
print(f"Consultation Fee : ₹{consultation:.2f}")
print(f"Room Charges     : ₹{room_charges:.2f}")
print(f"Medicine Charges : ₹{medicine_charges:.2f}")
print(f"Laboratory Fee   : ₹{lab_charges:.2f}")

print("-" * 45)
print(f"Subtotal         : ₹{subtotal:.2f}")
print(f"Discount         : ₹{discount:.2f}")
print("-" * 45)
print(f"TOTAL BILL       : ₹{total_bill:.2f}")
print("=" * 45)
print("       Thank you for choosing our hospital!")
print("=" * 45)

