
# Bus Passenger Occupancy Simulation

capacity = int(input("Enter bus capacity: "))

if capacity <= 0:
    print("Invalid bus capacity.")
else:
    stops = int(input("Enter number of bus stops: "))

    if stops < 0:
        print("Invalid number of stops.")
    else:
        passengers = 0

        for stop in range(1, stops + 1):
            print(f"\n--- Bus Stop {stop} ---")

            getting_off = int(
                input("Passengers getting off: ")
            )

            if getting_off < 0 or getting_off > passengers:
                print("Invalid number of passengers getting off.")
                print("Stop skipped.")
                continue

            passengers -= getting_off

            boarding = int(
                input("Passengers boarding: ")
            )

            if boarding < 0:
                print("Invalid boarding count.")
                print("Treating boarding as 0.")
                boarding = 0

            available = capacity - passengers

            if boarding > available:
                print("Bus is full!")
                print("Only", available, "passengers can board.")
                passengers = capacity
            else:
                passengers += boarding

            available = capacity - passengers
            occupancy = passengers / capacity * 100

            print("Current passengers:", passengers)
            print("Available seats:", available)
            print(f"Occupancy rate: {occupancy:.2f}%")

        print("\n===== FINAL BUS REPORT =====")
        print("Bus capacity:", capacity)
        print("Final passengers:", passengers)
        print("Available seats:", capacity - passengers)
        print(
            f"Final occupancy: "
            f"{passengers / capacity * 100:.2f}%"
        )
        print("============================")

