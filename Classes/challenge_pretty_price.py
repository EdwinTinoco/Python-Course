def pretty_price(num, extension):
    int_num = int(num)
    if '.' not in str(extension):
        result = extension * 0.01
    else:
        result = extension

    return int(num) + result

print(pretty_price(3.20, 99))    
print(pretty_price(3.2, .99))
print(pretty_price(3, .99))  


#Jordan example
def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))


#Ryan example
extension = extension * 0.01 if isinstance(extension, int) else extension