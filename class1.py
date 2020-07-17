
import math
import useful

try:
    from func1 import *
    import factor 
except:
    print("$ bash install.sh")
    exit()


class Constant:
    
    
    """
    >>> j=Constant()
    >>> j.pi()
    3.14159265358979323846
    >>> j=Constant(位数=5)
    >>> j.pi()
    3.14159
    >>> j.tau()
    
    """
     
    def __init__(self, 位数=20):
        self.位数 = 位数
        self.float_pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
        
    def pi(self):
        
        """返回pi的一定位数,精度可选"""
        
        return round(self.float_pi, self.位数)
        
    def tau(self):
        
        """返回tau的一定位数,精度可选"""
        
        return round(self.float_pi * 2, self.位数)
        
class Calculate:    

    """方便计算,所以开发"""
    
    def __init__(self,number):
        self.number = number
        
    def factor(self):
        
        """用列表推导式找因数"""
        
        return factor.factor(self.number)
        
    def _primer_number(self):
    
        return primer(self.number)
        
    def primer_number(self):
        
        """找一定范围的素数"""
        
        m = self.number
        
        return [i for i in Calculate(m)._primer_number()]
        
    def _composite_number(self):
                    
        return composite(self.number)
        
    def composite_number(self):
        
        """找一定范围的合数"""
        
        self.m = self.number
        
        return [i for i in Calculation(self.m)._composite_number()]

    def cofactor(self,number2):

        """找两个数所有的公因数"""

        self.number1 = self.number
        self.number2 = number2
        result = math.gcd(self.number1, self.number2)
        return Calculation(result).factor()

    def step_add(self):
        return useful.step_add(self.number)

    def dpf(self):
        return factor.dpf(self.number)
    
            
class Judge:
    
    """判断数的类型"""
    
    def isintert(self, number1, number2):
        
        """判断是否一个数为质数"""
        
        self.number1 = number1
        self.number2 = number2
        if type(self.number1) != int or type(self.num2) != int:
            print("必须是整数")
            exit()
        if math.gcd(self.number1, self.number2) == 1:
            return True
class Equation:
    """开发中的解方程类"""
    def solution(self, n, e):
    
        i = 0
        self.n = n
        self.e = float(e)
        while i < self.e:
        
            l = self.n.replace('x', str(i))
            if eval(l) == self.e:
            
                return i
            elif i == self.e:
            
                break
            else:
            
                print(i)
                i += 1
