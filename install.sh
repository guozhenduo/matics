gcc -fPIC -shared step.c -o step.so
pip install cython
python func1setup.py build_ext --inplace
python factorsetup.py build_ext --inplace
