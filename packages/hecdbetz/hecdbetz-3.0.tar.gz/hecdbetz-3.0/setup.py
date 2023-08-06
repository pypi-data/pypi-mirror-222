from distutils.core import  setup
import setuptools
packages = ['hecdbetz']# 唯一的包名，自己取名
setup(name='hecdbetz',
	version='3.0',
	author='zmw',
    packages=packages, 
    entry_points={
        'console_scripts': [
            'hecdbetz = hecdbetz.calculate:main',
        ],
    },
    package_dir={'requests': 'requests'},)
