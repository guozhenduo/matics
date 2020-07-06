# Matics
Matics is a math module. As the author has not translated the notes into English for the time being, please forgive me. But it's a bit good.

## Table of Contents
- [Matics](#Matics)
- [Lastest version](#Lastest-version)
- [Usage](#Usage)
  - [Step1](#Step1)
  - [Step2](#Step2)
- [Examples](#Examples)
- [Thanks-For-Who](#Thanks-For-Who)
- [FAQ](#FAQ)

## Latest Version
- 1.3.0
- 1.3.1
- 1.3.2rc1

## Usage
If you want to use past versions of this project, unzip the corresponding tar.xz file: `matics-+{desired_version}.tar.xz`

### Step1:
```
python func1setup.py build_ext --inplace
python factorsetup.py build_ext --inplace
```

### Step2:
```
python class1.py
python useful.py
python main.py
```

## Examples
```
>>> import matics.main as m 
>>> a1 = m.Constant(位数=5)
>>> print(a1.pi())

3.14159

>>> a2 = m.Constant(位数=6)
>>> print(a2)

3.141592

>>> a3 = m.Calculate(10)
>>> print(a3.factor())

[1, 2, 5, 10]

>>> a4 = m.Calculate(12)
>>> print(a4.factor())

[1, 2, 3, 4, 6, 12]
```
Author's email is [guozhenduo1@163.com](mailto:guozhenduo1@163.com). Welcome!!!

## *Thanks-For-Who*
I would like to thank Bangyen for making this project better.
## **FAQ**

1. Can I contribute?

 - That's for sure.As long as your code helps.
