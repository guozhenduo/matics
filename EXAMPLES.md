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
>>> 
```
