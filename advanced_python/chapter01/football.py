results = {
    'Iran': {'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0},
    'Portugal': {'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0},
    'Spain': {'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0},
    'Morocco': {'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0}
}

# Function to update team results
def update_results(team, goals_for, goals_against, result):
    results[team]['goal_difference'] += goals_for - goals_against
    
    if result == 'win':
        results[team]['wins'] += 1
        results[team]['points'] += 3
    elif result == 'lose':
        results[team]['loses'] += 1
    else:
        results[team]['draws'] += 1
        results[team]['points'] += 1

# Read match 
res0=input().split("-")
res1=input().split("-")
res2=input().split("-")
res3=input().split("-")
res4=input().split("-")
res5=input().split("-")

matches = [
    ('Iran', 'Spain', int(res0[0]),  int(res0[1])),
    ('Iran', 'Portugal',int(res1[0]),  int(res1[1])),
    ('Iran', 'Morocco', int(res2[0]),  int(res2[1])),
    ('Spain', 'Portugal', int(res3[0]),  int(res3[1])),
    ('Spain', 'Morocco', int(res4[0]),  int(res4[1])),
    ('Portugal', 'Morocco', int(res5[0]),  int(res5[1]))
]
for match in matches:
    team1, team2, goals1, goals2 = match
    
    if goals1 > goals2:
        update_results(team1, goals1, goals2, 'win')
        update_results(team2, goals2, goals1, 'lose')
    elif goals1 < goals2:
        update_results(team1, goals1, goals2, 'lose')
        update_results(team2, goals2, goals1, 'win')
    else:
        update_results(team1, goals1, goals2, 'draw')
        update_results(team2, goals2, goals1, 'draw')

# Sort and print results
sorted_results = sorted(results.items(), key=lambda x: (-x[1]['points'], -x[1]['wins'], -x[1]['goal_difference'],x[0]))

for team, team_data in sorted_results:
    wins = team_data['wins']
    loses = team_data['loses']
    draws = team_data['draws']
    goal_difference = team_data['goal_difference']
    points = team_data['points']
    
    print(f"{team} wins:{wins} , loses:{loses} , draws:{draws} , goal difference:{goal_difference} , points:{points}")