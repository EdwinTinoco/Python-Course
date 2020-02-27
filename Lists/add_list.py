tags = ['python', 'development', 'tutorials', 'code']

# Nope
# tags[-1] = 'Programming'

# In Place
tags.extend('Programming')
tags.extend(['Programming']) # para agregar un nuevo elemento al final de la lista

# New List
new_tags = tags + ['Programming']

print(new_tags)

print(tags)