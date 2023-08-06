from distutils.core import  setup
import setuptools
packages = ['hecdbetz']# 唯一的包名，自己取名
setup(name='hecdbetz',
	version='1.0',
	author='zmw',
    packages=packages, 
    package_dir={'requests': 'requests'},)
