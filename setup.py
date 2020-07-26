from setuptools import setup, find_packages

setup(
	name='matics',
	version="1.3.2b2",
	keyword=['math','mathematics'],
	author='suchenguo',
	author_email='guozhenduo1@163.com',
	description="一个包含矩阵，分数，计算，判断数类型，常量，方程的数学模块",
	packages=find_packages(),
	license="MIT lincense",
	install_requires=["Cython>=0.29.21"]
)
