class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
        
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res

# a constant function
p1 = Polynomial(42)

# a straight Line
p2 = Polynomial(0.75, 2)

# a third degree Polynomial
p3 = Polynomial(1, -0.5, 0.75, 2)

for i in range(1, 10):
    print(i, p1(i), p2(i), p3(i))