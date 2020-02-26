sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('q')
query_two = sentence.index('quick')
query_three = 'fox' in sentence

print(query)
print(query_two)
print(query_three)
