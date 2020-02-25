import operator
from functools import reduce

def dynamic_reducer(num_one, num_two, num_three, operator_symbol):
    if operator_symbol == "+":
        print("Operation: Addition")
        result = num_one + num_two  + num_three
        print(result)
    elif operator_symbol == "-":
        print("Operation: Sustraction")
        result = num_one - num_two - num_three
        print(result)
    elif operator_symbol == "*":
        print("Operation: Multiplication")
        result = num_one * num_two * num_three
        print(result)
    elif operator_symbol == "/":
        print("Operation: Division")
        result = num_one / num_two / num_three
        print(result)    
    

dynamic_reducer(1,2,3,"*")
