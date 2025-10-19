class Fraction:
    def __init__(self,x,y):
        self.numerator = x
        self.denominator = y

    def __str__(self):
         return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_denom = self.denominator * other.denominator

        return f"{new_num}/{new_denom}"

    def __sub__(self,other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_denom = self.denominator * other.denominator

        return f"{new_num}/{new_denom}"

    def __mul__(self,other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator  * other.denominator

        return f"{new_numerator}/{new_denominator}"
    def __truediv__(self,other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return f"{new_numerator}/{new_denominator}"



obj1 = Fraction(3,4)
obj2= Fraction(1,2)


print(obj1 + obj2) # lets make  addition for two fractions
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)