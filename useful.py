try:
    from functools import reduce
    from ctypes import CDLL
    so = CDLL("./step.so")
    #程序员:苏晨果
    #1.1.2版
    #来源:未知
    def step_add(m):
        if type(m) != int:
            print('类型必须为整数')
            exit()
        if m <= 65535:
            return so.step_add(m)
        else:
            return m + (m+1) // 2

except:
    print("Please inspect")
    exit()
