
import random
from datetime import datetime

# Railway Fare and Reservation Calculator

trains = {
    1: {"name": "Express Train", "fare": 150},
    2: {"name": "Superfast Express", "fare": 250},
    3: {"name": "AC Express", "fare": 500},
    4: {"name": "Premium Express", "fare": 800}
}

reservations = []


def display_trains():
    print("\n------ AVAILABLE TRAINS ------")
    print("Train No.  Train Name           Fare per person")
    for number, train in trains.items():
        print(f"{number:<11}{train['name']:<21}Rs. {train['fare']}")


def calculate_fare(train_number, passengers, class_type):
    base_fare = trains[train_number]["fare"]

    class_multiplier = {
        "Sleeper": 1.0,
        "AC 3 Tier": 1.5,
        "AC 2 Tier": 2.0,
        "AC First Class": 3.0
    }

    fare_per_person = base_fare * class_multiplier[class_type]
    total_fare = fare_per_person * passengers

    return fare_per_person, total_fare


def book_ticket():
    display_trains()

    try:
        train_number = int(input("\nEnter train number: "))

        if train_number not in trains:
            print("Invalid train number!")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Passenger name cannot be empty!")
            return

        age = int(input("Enter passenger age: "))
        if age <= 0 or age > 120:
            print("Please enter a valid age!")
            return

        source = input("Enter source station: ").strip()
        destination = input("Enter destination station: ").strip()

        if not source or not destination:
            print("Station names cannot be empty!")
            return

        if source.lower() == destination.lower():
            print("Source and destination must be different!")
            return

        journey_date = input("Enter journey date (DD-MM-YYYY): ")
        journey_date_obj = datetime.strptime(
            journey_date, "%d-%m-%Y"
        )

        if journey_date_obj.date() < datetime.today().date():
            print("Journey date cannot be in the past!")
            return

        passengers = int(input("Enter number of passengers: "))
        if passengers < 1 or passengers > 6:
            print("You can book 1 to 6 passengers per reservation.")
            return

        print("\nAvailable classes:")
        classes = ["Sleeper", "AC 3 Tier", "AC 2 Tier", "AC First Class"]

        for i, class_name in enumerate(classes, start=1):
            print(f"{i}. {class_name}")

        class_choice = int(input("Select class (1-4): "))

        if class_choice not in range(1, 5):
            print("Invalid class selection!")
            return

        class_type = classes[class_choice - 1]

        fare_per_person, total_fare = calculate_fare(
            train_number, passengers, class_type
        )

        pnr = random.randint(1000000000, 9999999999)

        reservation = {
            "pnr": pnr,
            "name": name,
            "age": age,
            "train": trains[train_number]["name"],
            "source": source,
            "destination": destination,
            "date": journey_date,
            "passengers": passengers,
            "class": class_type,
            "fare": total_fare
        }

        reservations.append(reservation)

        print("\n====== RESERVATION CONFIRMED ======")
        print(f"PNR Number       : {pnr}")
        print(f"Passenger Name   : {name}")
        print(f"Age              : {age}")
        print(f"Train            : {reservation['train']}")
        print(f"From             : {source}")
        print(f"To               : {destination}")
        print(f"Journey Date     : {journey_date}")
        print(f"Passengers       : {passengers}")
        print(f"Class            : {class_type}")
        print(f"Fare per person  : Rs. {fare_per_person:.2f}")
        print(f"Total Fare       : Rs. {total_fare:.2f}")
        print("===================================")

    except ValueError:
        print("Invalid input! Please enter the correct data.")


def view_reservation():
    try:
        pnr = int(input("\nEnter PNR number: "))

        for reservation in reservations:
            if reservation["pnr"] == pnr:
                print("\n------ RESERVATION DETAILS ------")
                for key, value in reservation.items():
                    print(f"{key.capitalize():<18}: {value}")
                return

        print("Reservation not found!")

    except ValueError:
        print("Please enter a valid PNR number.")


def cancel_reservation():
    try:
        pnr = int(input("\nEnter PNR number to cancel: "))

        for reservation in reservations:
            if reservation["pnr"] == pnr:
                reservations.remove(reservation)
                print("Reservation cancelled successfully!")
                return

        print("Reservation not found!")

    except ValueError:
        print("Please enter a valid PNR number.")


def main():
    while True:
        print("\n================================")
        print(" RAILWAY FARE AND RESERVATION")
        print("           CALCULATOR")
        print("================================")
        print("1. Display Available Trains")
        print("2. Book Ticket")
        print("3. View Reservation")
        print("4. Cancel Reservation")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_trains()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_reservation()
        elif choice == "4":
            cancel_reservation()
        elif choice == "5":
            print("Thank you for using the Railway Calculator!")
            break
        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()

