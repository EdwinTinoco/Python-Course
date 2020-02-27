teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

#una manera, sino se encuentra la llave que quieres borrar te manda un error
del teams['angels']

#mejor manera de borrar
removed_team = teams.pop('mets', 'Team not found')

print(teams)
print(removed_team)