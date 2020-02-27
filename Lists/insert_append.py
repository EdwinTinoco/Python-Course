"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(1, 'Anthony')

print(users)

users.append('Ian') #se usa cuando no importa el orden , se inserta al final

print(users)

print(users[2]) #regresa el valor sin brackets es decir un string
print([users[2]]) #regresa el valor con brackets es decir una lista con un solo elemento

users[4] = 'Brayden'

print(users)