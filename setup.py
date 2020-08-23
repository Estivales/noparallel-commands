#!/usr/bin/env python
import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

readme = open('README.rst').read()
history = open('HISTORY.rst').read()

setup(
    name='noparallel-commands',
    version=1.0,
    description='noparallel is a Django application that makes it easy to prevent parallel django commands execution.',
    long_description=readme + '\n\n' + history,
    author='Douglas Estivales',
    author_email='estivaless@gmail.com ',
    url='https://github.com/Estivales/noparallel-commands',
    packages=['noparallel-commands'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=3.1',
    ]
)