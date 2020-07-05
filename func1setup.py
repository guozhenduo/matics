from distutils.core import setup
from Cython.Build import cythonize

setup(name='matics func1  app',
      ext_modules=cythonize("func1.pyx"))
