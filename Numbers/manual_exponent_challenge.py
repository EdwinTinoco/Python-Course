#my code
def manual_exponent(num, exponent):    
    num_list = [num] * exponent  

    result = 1
    for i in num_list:
        result *= i
    return result

print(manual_exponent(10,2))

#Ryan example
def manual_exponent(num, exponent):  

    result = 1
    for x in range(exponent):
        result *= num

    return result

print(manual_exponent(10,2))


# Jordan example con loop
def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))



#Jordan example functional solution
from functools import reduce
def manual_exponent(num, exp):
    computed_list = [num] * exp
   
    return (reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))


#Ryan example
from functools import reduce
def reducer(total, element):
    return total * element

def manual_exponent(num, exp):
    computed_list = [num] * exp
   
    return (reduce(reducer, computed_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
