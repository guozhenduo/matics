from math import gcd 
class Fraction:
    def __init__(self, number1, number2):
        a1 = gcd(number1,number2)
        self.num1 = int(number1/a1)
        self.num2 = int(number2/a1)
    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.num1 + other + self.num2, self.num2)
        num_one = self.num1 * other.num2
        num_two = other.num1 * self.num2
        den = self.num2 + other.num2
        return Fraction(num_one + num_two, den)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(other * self.num1, other * self.num2)
        num = self.num1 * other.num1
        den = self.num2 * other.num2
        return Fraction(num, den)
    def __repr__(self):
        return f'Fraction({self.num1}, {self.num2})'
    def __str__(self):
        return f'{self.num1}/{self.num2}'
