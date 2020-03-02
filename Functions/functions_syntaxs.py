def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')



def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'secret')



def hundred():
  for num in range(1, 101):
    print(num)


hundred()



def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)