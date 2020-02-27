players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

#dict_keys, dict_values, dict_items son  dictionarie views object, no podemos tratarlos como una lista
print(players.keys())
print(players.values())
print(players.items())

# asi ya se puede usar como listas
print(list(players.values())[1])

player_names = list(players.copy().values())
print(player_names)



teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()
print(list(team_groupings))
#esto resulta
"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

print(list(team_groupings)[1][1][0])