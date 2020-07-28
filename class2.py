import math
import re

class Volume:
    def __init__(self, *args):
        args = list(args)
        for index in range(len(args)):
            item = args[index]
            if type(item) in [int, float]:
                if item < 0:
                    raise ValueError
            elif isinstance(item, str):
                if re.match('[0-9]+(.[0-9]+)?$', item):
                    if '.' in item:
                        args[index] = float(item)
                    else:
                        args[index] = int(item)
                else:
                    raise ValueError
            else:
                raise TypeError
        self.args = args if args else [0]
        self.dim = len(args)
    
    @staticmethod
    def product(args):
        prod = 1
        for item in args:
            prod *= item
        return prod
    
    @staticmethod
    def norm(val):
        return int(val) if int(val) == val else val

    @staticmethod
    def sphere(radius, dim):
        half = dim // 2
        if dim % 1:
            raise ValueError
        if dim % 2:
            fact = math.factorial(half) / math.factorial(dim)
            coeff = 2 * fact * 4 ** half
        else:
            coeff = 1 / math.factorial(half)
        pi_co = math.pi ** half
        return Volume.norm(coeff * pi_co * radius ** dim)
    
    def rectangle(self):
        return Volume.norm(Volume.product(self.args))
    
    def pyramid(self):
        vol = Volume.product(self.args) / self.dim
        return Volume.norm(vol)
