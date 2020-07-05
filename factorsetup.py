from distutils.core import setup
from Cython.Build import cythonize

setup(name='factor',
      ext_modules=cythonize("factor.pyx"))
