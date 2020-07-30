README.md in English
# Matics
Matics is a math module.  

## Table of Contents
- [Matics](#Matics)
- [Lastest version](#Lastest-version)
- [Usage](#Usage)
  - [Step1](##Step1)
- [Examples](#Examples)
- [Thanks-For-Who](#Thanks-For-Who)
- [Plan](#Plan)
- [FAQ](#FAQ)
- [Rely-On](#Rely-On)
## Latest Version
- 1.3.2b1


# Usage
See [DOCS.md](https://github.com/guozhenduo/matics/blob/master/help/DOCS.md)

## Step1:
```
Platform: Linux
$ cd matics
$ ./build.sh
Platform: Windows
D:\matics> pip install cython 
D:\matics> python func1setup.py build_ext --inplace
D:\matics> gcc -fPIC -shared step.c -o step.so
D:\matics> mv .matics/* ./
D:\matics> rmdir matics
D:\matics> python func1.pyx
D:\matics> python main.py
```

# Examples
Pleas look at [`EXAMPLES.md`](https://github.com/guozhenduo/matics/blob/master/help/EXAMPLES.md)

Author's email is [guozhenduo1@163.com](mailto:guozhenduo1@163.com). Welcome!!!

# *Thanks-For-Who*
I would like to thank [Bangyen](https://github.com/bangyen) for making this project better.
# Plan
No plan now.
# **FAQ**

1. Can I contribute?

 - That's for sure.As long as your code helps.

2. Which version is good?

 - 1.3.2b1

3. How do we update?

 - We update it every two weeks.

# Rely-On
- Python >= 3.8
- Gcc >= 10.0.0
- 

README.md in Chinese

# matics（为区别，所以首字母小写）
“matics”是个数学计算模块。

## 目录
- [版本](#版本)
- [使用](#使用)
  - [步骤1](##步骤1)
- [实例](#实例)
- [鸣谢](#鸣谢)
- [计划](#计划)
- [常见问题回答](#常见问题回答)

# 版本
- 1.3.2b1


# 使用
见[DOCS.md](https://github.com/guozhenduo/matics/blob/master/help/DOCS.md)
## 步骤1
```
操作系统: Linux
$ cd matics
$ ./build.sh
操作系统: Windows
D:\matics> pip install cython 
D:\matics> python func1setup.py build_ext --inplace
D:\matics> gcc -fPIC -shared step.c -o step.so
D:\matics> mv .matics/* ./
D:\matics> rmdir matics
D:\matics> python func1.pyx
D:\matics> python main.py
``` 

 # 实例
请看到[`EXAMPLES.md`](https://github.com/guozhenduo/matics/blob/master/help/EXAMPLES.md)


作者的邮箱是guozhenduo1@163.com，欢迎来信

# 鸣谢
感谢Bangyen，他为这个项目做出了巨大的贡献。

# 计划
目前没有计划。

# 常见问题回答

1. 我可以做贡献吗？

 - 肯定的。只要你的代码足够好。

2. 那个版本好？

 - 1.3.2b1

3. 我们如何更新？

 - 两周一次

# 依赖
- Python >= 3.8
- Gcc >= 10.0.0
- Cython >= 0.29.21
