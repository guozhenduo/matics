pip install cython
python func1setup.py build_ext --inplace
gcc -fPIC -shared step.c -o step.so
mv ./matics/*.so ./
rm -rf matics
