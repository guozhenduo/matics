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
        result = m + (m + 1) // 2 if m > 65535 else so.step_add(m)
        return result

except:
    print("Please inspect")
    exit()
