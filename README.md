README.md in English
# Matics
Matics is a math module.  But it's a bit good.

## Table of Contents
- [Matics](#Matics)
- [Lastest version](#Lastest-version)
- [Usage](#Usage)
  - [Step1](##Step1)
- [Examples](#Examples)
- [Thanks-For-Who](#Thanks-For-Who)
- [Plan](#Plan)
- [FAQ](#FAQ)

## Latest Version
- 1.3.0
- 1.3.1
- 1.3.2rc1
- 1.3.2rc2
- 1.3.2

# Usage
See DOCS.md

## Step1:
```bash
$ cd matics
$ ./install.sh
$ bash test.sh
```

#Examples
Pleas look at [`EXAMPLES.md`](https://github.com/guozhenduo/matics/blob/master/EXAMPLES.md)

Author's email is [guozhenduo1@163.com](mailto:guozhenduo1@163.com). Welcome!!!

# *Thanks-For-Who*
I would like to thank [Bangyen](https://github.com/bangyen) for making this project better.
# Plan
No plan now.
# **FAQ**

1. Can I contribute?

 - That's for sure.As long as your code helps.

2. Which version is good?

 - 1.3.2rc2

3. How do we update?

 - We update it every two weeks.


README.md in Chinese

# matics（为区别，所以首字母小写）
“matics”是个数学计算模块，我认为这个模块比较好。

## 目录
- [版本](#版本)
- [使用](#使用)
  - [步骤1](##步骤1)
- [实例](#实例)
- [鸣谢](#鸣谢)
- [计划](#计划)
- [常见问题回答](#常见问题回答)

#版本
 - 1.3.0
 - 1.3.1
 - 1.3.2rc1

#使用
见DOCS.md

 ##步骤1：
```bash
$ cd matics
$ bash install.sh
$ bash test.sh
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

 - 1.3.2rc2

3. 我们如何更新？

 - 两周一次
