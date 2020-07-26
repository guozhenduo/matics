Please look at [README.md](http://github.com/guozhenduo/matics/blob/master/README.md) before you look at this.
# Class Calculate
- in class1.py
```python
>>> import matics.main as m
>>> #__init__(self,number)
>>> u = m.Calculate(10)
>>> i = m.Calculate(number=20)
>>> u 
Calculate(10)
>>> i
Calculate(20)
>>> print(u)
10
>>> print(i)
20
>>> #factor(self)
>>> u.factor()
[1,2,5,10]
>>> i.factor()
[1,2,4,5,10,20]
>>> #primer_number(self)
>>> u.primer_number()
[2,3,5,7]
>>> i.primer_number()
[2,3,5,7,11,13,17,19]
>>> u.step_add()
55
>>> i.step_add()
210
>>> # acfactor(self,number)
>>> # all common factor
>>> u.acfactor(i)
[1,2,5,10]
>>> i.acfactor(30)
[1,2,5,10]
>>> #composite_number(self)
>>> u.composite_number()
[4,6,8,9,10]
>>> i.composite_number()
[4,6,8,9,10,12,14,15,16,18,20]
>>> #primef(self)
>>> #prime_factor
>>> u.primef()
[2,5]
>>> i.primef()
[2,5]
>>> # least_cm(self,num)
>>> u.least_cm(20)
10
>>> i.least_cm(45)
5
>>> 
```
# Class Constant
- in class1.py 
```python
>>> from class1 import Constant
>>> # __init__(self,num=20)
>>> j=Constant()
>>> # pi(self)
>>> j.pi()
3.14159265358979323846
>>> j=Constant(num=5)
>>> j.pi()
3.14159
>>> # tau(self)
>>> j.tau()
6.28318
>>> 
```

# Class Judge
- in class1.py 
```python
>>> from class import Judge
>>> # __init__(self,number1,number2)
>>> l = Judge(3,17)
>>> # isprimer(self)
>>> l.isprimer()
True
>>> u = Judge(4,8)
>>> u.isprimer()
False
```

# Class Equation
- in class1.py
```python
>>> from class1 import Equation
>>> # __init__(self,x)
>>> u = Equation("x")
>>> u.solution("3*x",18)
6
>>> u.solution("5+x",6)
1
```

# Class Fraction
- in statistics.py
```python
>>> from statistics import Fraction
>>> # __init__(self,num1 = 0,num2 = 1,reduce=True)
>>> u = Fraction(4,8)
>>> u
Fraction(1,2)
>>> print(u)
1/2
>>> Fraction(2)
Fraction(2,1)
>>> Fraction(62,84)
Fraction(31,42)
>>> Fraction(62,84,False)
Fraction(62,84)
```
