pip install cython
python func1setup.py build_ext --inplace
if [ ! -f "../step.c"]; then 
	gcc -fPIC -shared step.c -o step.so
	else 
	g++ -fPIC -shared step.cpp -o step.so
fi
mv ./matics/*.so ./
rm -rf matics
