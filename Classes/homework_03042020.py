"""
Build three classes.
 -Two of which must inherit from the first and employ polymorphism. 
 -Between the three classes there must be at least: 
    -5 methods 
    -3 instance attributes
    -1 class attribute. 
 -Each class should have a dunder str and dunder repr, and the parent class should have a dunder init.
 """

class Some_Operations:
    title = "***** Addition and Sustraction Operations *****"

    def __init__(self, description, operator_symbol, num1 = 6, num2 = 3):
        self.description = description
        self.operator_symbol = operator_symbol
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.description} use this symbol: '{self.operator_symbol}'"

    def __repr__(self):
        return f"\n<({self.description})> <('{self.operator_symbol}')>"

    def operations(self):             
        raise NotImplementedError("Subclass must implement operations method")

class Addition(Some_Operations):  
    def operations(self):
        return f'\nEjemplo: {self.num1} + {self.num2} = {self.num1 + self.num2}'
    
class Sustraction(Some_Operations):
    def operations(self):
        return f'\nEjemplo: {self.num1} - {self.num2} = {self.num1 - self.num2}'

add_op = Addition("The addition operation", "+")
sus_op = Sustraction("The sustraction operation", "-")

print(add_op.title)
print(str(add_op), repr(add_op), add_op.operations())
print(str(sus_op),repr(sus_op), sus_op.operations())