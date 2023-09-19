import random

class Human:
    def __init__(self, name):
        self.name = name

class FootballPlayer(Human):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

# Create FootballPlayer objects
football_players = [
    FootballPlayer("حسین", None), FootballPlayer("مازیار", None), FootballPlayer("اکبر", None),
    FootballPlayer("نیما", None), FootballPlayer("مهدی", None), FootballPlayer("فرهاد", None),
    FootballPlayer("محمد", None), FootballPlayer("خشایار", None), FootballPlayer("میلاد", None),
    FootballPlayer("مصطفی", None), FootballPlayer("امین", None), FootballPlayer("سعید", None),
    FootballPlayer("پویا", None), FootballPlayer("پوریا", None), FootballPlayer("رضا", None),
    FootballPlayer("علی", None), FootballPlayer("بهزاد", None), FootballPlayer("سهیل", None),
    FootballPlayer("بهروز", None), FootballPlayer("شهروز", None), FootballPlayer("سامان", None),
    FootballPlayer("محسن", None)
]


team_a = random.sample(football_players, k=11)
team_b = [player for player in football_players if player not in team_a]


# Assign teams to players
for player in team_a:
    player.team = 'A'
for player in team_b:
    player.team = 'B'

# Print the team names for each player
for player in football_players:
    print(player.name, player.team)
