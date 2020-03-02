"""
function
looping
conditionals
math operators
"""

def fizzbuzz(max_value):
    first_multiple = 3
    second_multiple = 5
    collection = []
    
    for num in range(1, max_value + 1):
        if (num % first_multiple == 0) and (num % second_multiple == 0):
            collection.append('FizzBuzz')
        elif (num % first_multiple == 0):
            collection.append('Fizz')
        elif (num % second_multiple == 0):
            collection.append('Buzz')
        
        else:
            collection.append(num)

    return collection


print(fizzbuzz(100))


#Jordan solucion
def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)



