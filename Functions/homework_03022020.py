# 1) Write a function that generates a random hexadecimal color code
# ex output => #00c274

from random import *

def hexadecimal_number(num):
    return f"#{str(hex(num)).lstrip('0x')}"


print(hexadecimal_number(randint(1000000,9999999)))


#Ryan example
from random import *
def random_hex():
    hex_values = list("ABCDEF") + list(range(10))
    final_hex = []
    i = 1

    while i <= 6:
        final_hex.append(str(hex_values[randinit(0,15)]))
        i += 1

    return f"#{''.join(final_hex)}"


print(random_hex())



# 2) Write a function that takes in a string separated by hyphens and prints the words in a 
# hyphen-separated sequence after sorting them alphabetically.
# ex: "green-red-black-white" => "black-green-red-white"

def sort_string(string):
    string_list = []    
    word = ''    
    counter = 0    

    for letter in string:
        counter += 1
        if counter == len(string):
            word += letter
            string_list.append(word)
        elif letter != '-':
            word += letter
        else:
            string_list.append(word)
            word = ''

    string_list.sort()
    return "-".join(string_list)


print(sort_string('green-yellow-red-black-white-teal-brown'))



# #Ryan example
def sort_string(string):
    split_list = string.split("-")
    split_list.sort()
    return "-".join(split_list)

print(sort_string('green-yellow-red-black-white-teal-brown'))


