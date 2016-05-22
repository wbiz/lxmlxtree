
from codecs import open
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lxmlxtree',
    version='0.0.1',

    description='A lxml helper class to insert element or wrap element to a certain text',
    long_description=long_description,

    url='https://github.com/wbiz/lxmltree',

    author='Wbiz',
    author_email='wbiz9999@gmail.com',

    license='BSD',


    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='lxml wrap insert pi element encoding serialise',

    py_modules=["lxmlxtree"],


)