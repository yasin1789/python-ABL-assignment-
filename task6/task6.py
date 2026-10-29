
# Sports Tournament Ranking System

teams = {}

n = int(input("Enter the number of teams: "))

# Input team names
for i in range(n):
    name = input(f"Enter team {i + 1} name: ")
    teams[name] = {
        "points": 0,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0
    }

matches = int(input("Enter the number of matches: "))

# Input match results
for i in range(matches):
    print(f"\nMatch {i + 1}")

    team1 = input("Enter first team: ")
    team2 = input("Enter second team: ")

    if team1 not in teams or team2 not in teams or team1 == team2:
        print("Invalid teams. Match skipped.")
        continue

    score1 = int(input(f"Enter {team1} score: "))
    score2 = int(input(f"Enter {team2} score: "))

    if score1 < 0 or score2 < 0:
        print("Scores cannot be negative. Match skipped.")
        continue

    teams[team1]["played"] += 1
    teams[team2]["played"] += 1

    teams[team1]["goals_for"] += score1
    teams[team1]["goals_against"] += score2

    teams[team2]["goals_for"] += score2
    teams[team2]["goals_against"] += score1

    if score1 > score2:
        teams[team1]["points"] += 3
        teams[team1]["wins"] += 1
        teams[team2]["losses"] += 1

    elif score2 > score1:
        teams[team2]["points"] += 3
        teams[team2]["wins"] += 1
        teams[team1]["losses"] += 1

    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1
        teams[team1]["draws"] += 1
        teams[team2]["draws"] += 1

# Rank teams by points, then goal difference
ranking = sorted(
    teams.items(),
    key=lambda item: (
        item[1]["points"],
        item[1]["goals_for"] - item[1]["goals_against"],
        item[1]["goals_for"]
    ),
    reverse=True
)

# Display ranking
print("\n========== TOURNAMENT RANKING ==========")
print(f"{'Rank':<6}{'Team':<15}{'P':<5}{'W':<5}{'D':<5}{'L':<5}{'Pts':<6}{'GD':<5}")

for rank, (name, data) in enumerate(ranking, start=1):
    goal_difference = data["goals_for"] - data["goals_against"]

    print(
        f"{rank:<6}{name:<15}{data['played']:<5}"
        f"{data['wins']:<5}{data['draws']:<5}"
        f"{data['losses']:<5}{data['points']:<6}"
        f"{goal_difference:<5}"
    )

if ranking:
    print("\nTournament Winner:", ranking[0][0])

print("========================================")
