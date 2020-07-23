import math
import re
from class1 import Calculate

class Fraction:

    def __init__(self, num1=0, num2=1, reduce=True):

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

            div = math.gcd(num1, num2) ** reduce
            self.num1 = num1 // div
            self.num2 = num2 // div

        else:

            num2 = num2 if num1 else 1
            self.num1 = [float, int][num1 == int(num1)](num1)
            self.num2 = [float, int][num2 == int(num2)](num2)
        self.num = self.num1 / self.num2
        
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

    def __eq__(self, other):
        return (self.num1 * other.num2) == (other.num1 * self.num2)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if type(other) in [int, float]:
            other = Fraction(other)
        return (self.num1 * other.num2) < (other.num1 * self.num2)

    def __gt__(self, other):
        return not (self <= other)

    def __le__(self, other):
        return (self == other) or (self < other)

    def __ge__(self, other):
        return not (self < other)

    def __round__(self, number=0):
        return Fraction(round(self.num1 / self.num2, number))

    def __mod__(self, other):
        return (self.num1 / self.num2) % (other.num1 / other.num2 )

    def reduction(self, other):
        # reduction of fractions to a common denominator
        lcm = Calculate(self.num2).least_cm(other.num2)
        self.num1, other.num1 = lcm // self.num2, lcm // other.num2 
        self.num2, other.num2 = lcm, lcm
        return [self, other]
        
    def is_improper(self):
        return self > Fraction(1)   

    def to_percentage(self):
        one = 100 / self.num2
        two = self.num1 * one
        percentage = Percentage(two)
        return percentage


class Percentage:

    def __init__(self, num):
        if num < 0:
            raise TypeError

        if isinstance(num, str):
            if "%" in num:
                try:    
                    num = int(num.replace("%", ""))
                except:
                    num = float(num.replace("%", ""))

        if isinstance(num, Fraction):
            one = 100 / num.num2
            num.num1 *= one
            num.num2 = 100
            num = num.num1 


        try:
            if num == int(num):
                num = int(num)
            else:
                num = float(num)
        except:
            raise TypeError("Error num!")
        
        self.num = num
        self.float_fraction = num / 100

    def __add__(self, other):
        return Percentage(self.num + other.num)

    def __repr__(self):
        return f"Percentage({self.num})"

    def __str__(self):
        return f"{self.num}%"
    
    def __sub__(self, other):
        return Percentage(self.num - other.num)

    def __div__(self, other):
        if not other.num:
            raise ZeroDivisionError
        return Percentage(self.num / other.num)

    def __mul__(self, other):
        return Percentage(self.num * other.num)

    def __mod__(self, other):
        return Percentage(self.num % other.num)

    def __eq__(self, other):
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num

    def __lt__(self, other):
        return self.num < other.num

    def __gt__(self, other):
        return self.num > other.num

    def to_fraction(self):
        return Fraction(num, 100, False)

