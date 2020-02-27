"""
Write me a program that reverse a word
Ex: ryan => nayr
"""

def reverse_word(word):
    result = ""

    word_to_list = list(word)
    print(word_to_list)

    for letter in range(len(word_to_list)):
        result += word_to_list.pop()
        
    return result

print(reverse_word('Basketball'))


#Ryan example
def reversed_word(word): 
    return word[::-1] 
    
print(reversed_word("Lucy"))