try:
    from functools import reduce
    from ctypes import CDLL
    so = CDLL("./step.so")
    #程序员:苏晨果
    #1.1.2版
    #来源:未知
    def step_add(m):
        if type(m) != int:
            print('类型必须为浮点数')
            exit()
        if m <= 65535:
            return so.step_add(m)
        else:
            return m * (m + 1) // 2
    def step_mul(step_max):
        l = (i for i in range(1, step_max + 1))
        return reduce(lambda x, y: x * y, l)
    #程序员:苏晨果
    #1.0.2版
    #来源:terminal
    def tenimal():
        while True: 
            l = input('>>> ')
            exec(l)
            if l == ' ':
                break
                exit()

except:
    print("Please inspect")
    exit()
