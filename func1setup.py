from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='func1.pyx',
    ext_modules=cythonize("func1.pyx")
)
