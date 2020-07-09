README.md for English
# Matics
Matics is a math module. As the author has not translated the notes into English for the time being, please forgive me. But it's a bit good.

## Table of Contents
- [Matics](#Matics)
- [Lastest version](#Lastest-version)
- [Usage](#Usage)
  - [Step1](##Step1)
  - [Step2](##Step2)
- [Examples](#Examples)
- [Thanks-For-Who](#Thanks-For-Who)
- [Plan](#Plan)
- [FAQ](#FAQ)

## Latest Version
- 1.3.0
- 1.3.1
- 1.3.2rc1

# Usage
If you want to use past versions of this project, unzip the corresponding tar.xz file: `matics-+{desired_version}.tar.xz`

## Step1:
```bash
$ python func1setup.py build_ext --inplace
$ python factorsetup.py build_ext --inplace
```

## Step2:
```bash
$ python class1.py
$ python useful.py
$ python main.py
```

# Examples
```python
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

# *Thanks-For-Who*
I would like to thank [Bangyen](https://github.com/bangyen) for making this project better.
# Plan
No plan now.
# **FAQ**

1. Can I contribute?

 - That's for sure.As long as your code helps.

2. Which version is good?

 - 1.3.1


Chinese README.md

# matics（为区别，所以首字母小写）
“matics”是个数学计算模块，我认为这个模块比较好。

## 目录
- [版本](#版本)
- [使用](#使用)
  - [步骤1](##步骤1)
  - [步骤2](##步骤2)
- [实例](#实例)
- [鸣谢](#鸣谢)
- [计划](#计划)
- [常见问题回答](#常见问题回答)

#版本
 - 1.3.0
 - 1.3.1
 - 1.3.2rc1

#使用
如果你想使用过去版本，请解压matics-加版本.tar.xz。
 ##步骤1：
```bash
$ python func1setup.py build_ext --inplace
$ python factorsetup.py build_ext --inplace
```

## 步骤2:
```bash
$ python class1.py
$ python useful.py
$ python main.py
```
 # 实例
```python
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
作者的邮箱是guozhenduo1@163.com，欢迎来信

# 鸣谢
感谢Bangyen，他为这个项目做出了巨大的贡献。

# 计划
目前没有计划。

# 常见问题回答

1. 我可以做贡献吗？
 - 肯定的。只要你的代码足够好。
2. 那个版本好？
 - 1.3.1
