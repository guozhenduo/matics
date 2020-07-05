try:
    from class1 import *
except:
    raise ImportError("File 'class1.py' can't exist!")
    exit()
