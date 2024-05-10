# Class for 2x2 matrix
# |a b|
# |c d|
class TwoByTwoMatrix():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        d = self.d + other.d
        return TwoByTwoMatrix(a, b, c, d)
    
    def __mul__(self, other):
        a = self.a * other.a + self.b * other.c
        b = self.a * other.b + self.b * other.d
        c = self.c * other.a + self.d * other.c
        d = self.c * other.b + self.d * other.d
        return TwoByTwoMatrix(a, b, c, d)
    
    def __repr__(self):
        return "|{} {}|\n|{} {}|".format(self.a, self.b, self.c, self.d)
    
mat_a = TwoByTwoMatrix(1, 1, 1, 1)
mat_b = TwoByTwoMatrix(2, 4, 5, 6)

print(mat_a+mat_b)
print(mat_a*mat_b)