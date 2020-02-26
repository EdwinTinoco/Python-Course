# Challenge 1: Find the Length of a String
# ex: "The" => 3

def lenght_string(string):
    return len(string)

print(lenght_string('Some string'))

# --------------------------------------------------------------------------------------------------------
# Challenge 2: Create One String From Multiple Strings
# ex: 
# string1 = "the"
# string2 = "dog"
# output => "the dog"

def long_string(string_list):
    result = ""
    for string in string_list:
        result += string + " "
        
    return result.strip()

print(long_string(['I','hope','Utah','Jazz', 'will', 'go', 'to', 'the', 'playoffs']))

# --------------------------------------------------------------------------------------------------------
# Challenge 3: Swap first and last characters in a string
# Ex: "the dog" => "ghe doT"
# "ABCD" => "DBCA"
# "WINDOWS" => "SINDOWW"

def swap_letters(string):    
    middle_letters = ""
    i = 1

    print(string)

    for letter in string:    
        if (i == 1):
            first_letter = letter
        elif (i > 1) & (i == len(string)):
            last_letter = letter
        elif (i > 1):
            middle_letters += letter

        i += 1

    return last_letter + middle_letters + first_letter           

print(swap_letters('The dog'))

# --------------------------------------------------------------------------------------------------------
# Challenge 4: Sum all items in a list
# EX: [1, 2, 3] => 6

import operator
from functools import reduce

def sum_items_list(collection, op):
    operators = {
        "+": operator.add       
    }
    return reduce((lambda total, element: operators[op](total, element)), collection)

print(sum_items_list([1,2,3], "+"))

# --------------------------------------------------------------------------------------------------------
# Challenge 5: Take list of words and return the longest one along with its length:
# EX: ["PHP", "Backend", "Exercises"]
# output => Longest Word: Exercises, Length: 9

def long_short_word(words):    
    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        if len(word) >= len(longest_word):
            longest_word = word
            longest_len = len(word)
        elif len(word) <= len(shortest_word):
            shortest_word = word
            shortest_len = len(word)
    
    # return "Longest word: " + longest_word +", "+ "Lenght: " + str(longest_len), "Shortest word: " + shortest_word +", "+ "Lenght: " + str(shortest_len)
    print("Longest word: " + longest_word +", "+ "Lenght: " + str(longest_len))
    print("Shortest word: " + shortest_word +", "+ "Lenght: " + str(shortest_len))

# print(long_short_word(['Iteration', 'House', 'two', 'Convention']))
long_short_word(['Iteration', 'House', 'two', 'Convention'])

#Otro ejemplo
# def return_longest(string_list):
#     longest_word = string_list[0]

#     for word in string_list:
#         if len(word) > len(longest_word):
#             longest_word = word
    
#     return f"""
#     Longest: {longest_word}
#     Lenght: {len(longest_word)}
#     """.strip()

# print(return_longest('Iteration', 'House', 'two', 'Convention'))



# --------------------------------------------------------------------------------------------------------
# Challenge 6: Replace all occurrences of the first letter in string with '$' EXCEPT for the first letter itself.
# EX: "racecar" => "raceca$"
# "retrofit" => "ret$ofit"
# "talkative" => "talka$ive"
# "bobby" => "bo$$y"

def occurrences(word):
    count = 0
    first_letter = word[0]

    len_string = len(word)
    
    for i in range(len(word)):
        if (i < (len(word)) - 1):
            if (first_letter == word[i+1]):
                count += 1
        elif (i == (len(word)) - 1):
            if (first_letter == word[i]):
                count += 1
    
    if (count > 0):
        result = word.replace(first_letter, "$")
        print(result)
    else:
        print("There's no ocurrences in the string")
            
occurrences('retrofit')

#otro ejemplo
def custom_split(string):
  return [char for char in string]

def character_replace(string):
  split_list = custom_split(string)
  second_list = split_list[1:]

  for letter in second_list:
    if letter == split_list[0]:
      idx = second_list.index(letter)
      second_list[idx] = "$"

  return f'{split_list[0]}{"".join(second_list)}'


print(character_replace("retrofitter"))



            


