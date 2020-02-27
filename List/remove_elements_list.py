users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop() #elimina el ultimo item y retorna el valor del item por si lo quieres accesar

print(popped_user)
print(users)

del users[0]

print(users)