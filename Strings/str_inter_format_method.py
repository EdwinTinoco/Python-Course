name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

# greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}...- {3}".format(name, age, product,"Jordan")

greeting = f"Hi {name}, you are listed as {age} years old and you have purchased: {product}...- {from_account}".format(name, age, product,from_account)

print(greeting)