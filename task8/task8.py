
# Library Borrowing and Fine Reconciliation

from datetime import datetime

FINE_PER_DAY = 5
LOAN_PERIOD = 14

borrowed_books = {}

n = int(input("Enter number of books to borrow: "))

# Record borrowed books
for i in range(n):
    print(f"\nBook {i + 1}")

    book_id = input("Enter book ID: ")
    book_name = input("Enter book name: ")
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
    return_date = input("Enter return date (YYYY-MM-DD): ")

    try:
        borrowed = datetime.strptime(borrow_date, "%Y-%m-%d")
        returned = datetime.strptime(return_date, "%Y-%m-%d")

        if returned < borrowed:
            print("Invalid dates: return date is before borrow date.")
            continue

        days_borrowed = (returned - borrowed).days
        overdue_days = max(0, days_borrowed - LOAN_PERIOD)
        fine = overdue_days * FINE_PER_DAY

        borrowed_books[book_id] = {
            "name": book_name,
            "borrow_date": borrow_date,
            "return_date": return_date,
            "days": days_borrowed,
            "overdue": overdue_days,
            "fine": fine
        }

    except ValueError:
        print("Invalid date format. Book record skipped.")

# Reconcile fine payments
print("\n===== LIBRARY FINE RECONCILIATION =====")

total_fines = 0
total_paid = 0
total_outstanding = 0

for book_id, book in borrowed_books.items():
    print(f"\nBook: {book['name']} (ID: {book_id})")
    print("Days borrowed:", book["days"])
    print("Overdue days:", book["overdue"])
    print(f"Fine amount: Rs. {book['fine']:.2f}")

    paid = float(input("Enter fine amount paid: "))

    if paid < 0:
        print("Invalid payment. Treating payment as zero.")
        paid = 0

    if paid > book["fine"]:
        print("Payment exceeds fine. Excess amount excluded.")
        paid = book["fine"]

    outstanding = book["fine"] - paid

    print(f"Fine paid: Rs. {paid:.2f}")
    print(f"Outstanding fine: Rs. {outstanding:.2f}")

    total_fines += book["fine"]
    total_paid += paid
    total_outstanding += outstanding

print("\n========== FINAL SUMMARY ==========")
print("Books processed:", len(borrowed_books))
print(f"Total fines: Rs. {total_fines:.2f}")
print(f"Total payments: Rs. {total_paid:.2f}")
print(f"Outstanding fines: Rs. {total_outstanding:.2f}")
print("===================================")
