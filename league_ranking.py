import sys
from collections import defaultdict
import re

def calculate_league_ranking(input_lines):

    team_points = defaultdict(int)
    all_teams = set()

    for line in input_lines:
        team1, score1, team2, score2 = parse_line(line)
        all_teams.update([team1, team2])  

        if score1 > score2:  
            team_points[team1] += 3
        elif score1 < score2: 
            team_points[team2] += 3
        else:  
            team_points[team1] += 1
            team_points[team2] += 1 

    for team in all_teams:
        if team not in team_points:
            team_points[team] = 0

    sorted_teams = sorted(team_points.items(), key=lambda x: (-x[1], x[0]))

    result = []
    rank = 0
    last_points = None
    for i, (team, points) in enumerate(sorted_teams, 1):
        if points != last_points:
            rank = i
        last_points = points
        suffix = "pt" if points == 1 else "pts"
        result.append(f"{rank}. {team}, {points} {suffix}")

    return "\n".join(result)


def parse_line(line):
    match = re.match(r"(.+) (\d+), (.+) (\d+)", line)
    if not match:
        raise ValueError(f"Invalid input format: {line}")
    team1, score1, team2, score2 = match.groups()
    return team1.strip(), int(score1), team2.strip(), int(score2)

def get_input_from_user():
    print("Please enter the match results (one per line). Type 'done' when you are finished:")
    input_lines = []
    
    while True:
        line = input()
        if line.lower() == 'done':
            break
        input_lines.append(line)
    
    return input_lines

def get_input_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            input_lines = file.read().strip().split("\n")
        return input_lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)  

if __name__ == "__main__":
    choice = input("Do you want to provide a file path (type 'file') or string data (type 'string')? ").strip().lower()
    
    if choice == "file":
        file_path = input("Please enter the file path: ").strip()
        input_lines = get_input_from_file(file_path)
    elif choice == "string":
        input_lines = get_input_from_user()
    else:
        print("Invalid choice. Please type 'file' or 'string'.")
        sys.exit(1)  

    print(calculate_league_ranking(input_lines))