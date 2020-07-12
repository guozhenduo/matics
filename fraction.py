import math
import re


class Fraction:
    def __init__(self, num1=0, num2=1):
        if not ({type(num1), type(num2)} - {int, float, str}):
            if type(num1) != str and type(num2) == str:
                raise TypeError
        if isinstance(num1, str):
            regex = '-?[0-9]+(.[0-9]+)?'
            if re.match(f'^{regex}/{regex}$', num1):
                num1, num2 = num1.split('/')
                num1 = [int, float]['.' in num1](num1)
                num2 = [int, float]['.' in num2](num2)
            else:
                raise TypeError
        if not num2:
            raise ZeroDivisionError
        if isinstance(num1, int) and isinstance(num2, int):
            div = math.gcd(num1, num2)
            self.num1 = num1 // div
            self.num2 = num2 // div
        else:
            num2 = num2 if num1 else 1
            self.num1 = [float, int][num1 == int(num1)](num1)
            self.num2 = [float, int][num2 == int(num2)](num2)

    def __neg__(self):
        sign = sum([self.num1 > 0, self.num2 > 0, 1]) % 2
        return Fraction(-1 ** sign * abs(self.num1), abs(self.num2))

    def __sub__(self, other):
        return self + -other

    def __add__(self, other):
        if type(other) in [int, float]:
            return Fraction(self.num1 + other * self.num2, self.num2)
        num_one = self.num1 * other.num2
        num_two = other.num1 * self.num2
        den = self.num2 * other.num2
        return Fraction(num_one + num_two, den)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Fraction(other * self.num1, self.num2)
        num = self.num1 * other.num1
        den = self.num2 * other.num2
        return Fraction(num, den)

    def __truediv__(self, other):
        return self * Fraction(other.num2, other.num1)

    def __int__(self):
        return self.num1 // self.num2

    def __float__(self):
        return self.num1 / self.num2

    def __repr__(self):
        return f'Fraction({self.num1}, {self.num2})'

    def __str__(self):
        return f'{self.num1}/{self.num2}'
