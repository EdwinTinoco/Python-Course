"""
Write me a program takes a string and sort the letters
"""

def sort_string(string):
    new_string = string.lower()  
    print(new_string)

    string_list = list(new_string)  
    print(string_list)

    print(sorted(string_list))

print(sort_string('Hi There'))

#otro ejemplo
def sort_string(string):
    return "".join(sorted(string, key=lambda x: x.lower())).strip()

print(sort_string('Hi There'))

#otro ejemplo
def alphabetical_order(string):
    return "".join(sorted(string.lower())).strip()

print(alphabetical_order(' Hi There'))