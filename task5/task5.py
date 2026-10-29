
# Student Timetable Conflict Detection

timetable = []

n = int(input("Enter the number of classes: "))

# Input timetable details
for i in range(n):
    print(f"\nEnter details for class {i + 1}")

    subject = input("Enter subject name: ")
    day = input("Enter day: ").strip().lower()
    start = int(input("Enter start time (24-hour format, e.g. 9 for 09:00): "))
    end = int(input("Enter end time (e.g. 10 for 10:00): "))

    if start >= end or start < 0 or end > 24:
        print("Invalid time. Please enter valid class times.")
        continue

    timetable.append({
        "subject": subject,
        "day": day,
        "start": start,
        "end": end
    })

# Detect conflicts
conflict_found = False

print("\n===== TIMETABLE CONFLICT REPORT =====")

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):

        class1 = timetable[i]
        class2 = timetable[j]

        # Check same day and overlapping times
        if (class1["day"] == class2["day"]
                and class1["start"] < class2["end"]
                and class2["start"] < class1["end"]):

            print(
                f"Conflict: {class1['subject']} "
                f"({class1['start']}:00-{class1['end']}:00) "
                f"and {class2['subject']} "
                f"({class2['start']}:00-{class2['end']}:00) "
                f"on {class1['day'].capitalize()}"
            )
            conflict_found = True

if not conflict_found:
    print("No timetable conflicts detected.")

print("====================================")
