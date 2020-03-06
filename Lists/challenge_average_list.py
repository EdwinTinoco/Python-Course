#Calcular el average de lista
num_list = [1, 2, 3, 4, 5, 6]

def average_list(num_list):    
    result = 0

    for num in num_list:
        result += num

    return f"The average from the list is: {result/len(num_list)}"

print(average_list(num_list))


#Jordan solution
from functools import reduce
def get_average(num_list):
    total = reduce(
            (lambda total, element: total + element),
            num_list)

    return total/len(num_list)


num_list = [1, 2, 3, 4, 5, 6]
print(get_average(num_list))


#Ryan solution
def get_average(*args):
    return sum(args) / len(args)
    

print(get_average(1,2,3,4,5,6))

    