
# Campus Event Seating and Entry Validation

print("===== CAMPUS EVENT MANAGEMENT =====")

capacity = int(input("Enter total seating capacity: "))

if capacity <= 0:
    print("Invalid seating capacity.")
else:
    attendees = {}
    occupied_seats = 0

    while True:
        print("\n1. Register attendee")
        print("2. Validate entry")
        print("3. View seating status")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            ticket_id = input("Enter ticket ID: ").strip()
            name = input("Enter attendee name: ").strip()

            if not ticket_id or not name:
                print("Ticket ID and name are required.")
                continue

            if ticket_id in attendees:
                print("Ticket ID already registered.")
                continue

            if occupied_seats >= capacity:
                print("Event is full. No seats available.")
                continue

            seat_number = occupied_seats + 1

            attendees[ticket_id] = {
                "name": name,
                "seat": seat_number,
                "entered": False
            }

            occupied_seats += 1

            print("Registration successful!")
            print("Attendee:", name)
            print("Assigned seat:", seat_number)

        elif choice == "2":
            ticket_id = input("Enter ticket ID: ").strip()

            if ticket_id not in attendees:
                print("Invalid ticket. Entry denied.")

            elif attendees[ticket_id]["entered"]:
                print("Duplicate entry detected. Entry denied.")

            else:
                attendees[ticket_id]["entered"] = True
                print("Entry validated successfully!")
                print("Welcome,", attendees[ticket_id]["name"])
                print("Seat number:", attendees[ticket_id]["seat"])

        elif choice == "3":
            entered_count = sum(
                attendee["entered"]
                for attendee in attendees.values()
            )

            print("\n===== SEATING STATUS =====")
            print("Total capacity:", capacity)
            print("Registered attendees:", len(attendees))
            print("Occupied seats:", occupied_seats)
            print("Available seats:", capacity - occupied_seats)
            print("Entries validated:", entered_count)

        elif choice == "4":
            print("\n===== FINAL EVENT REPORT =====")
            print("Total registered:", len(attendees))
            print("Seats occupied:", occupied_seats)
            print("Seats available:", capacity - occupied_seats)
            print(
                "Entries validated:",
                sum(a["entered"] for a in attendees.values())
            )
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")
