# To use a consistent encoding
from codecs import open
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lxmlxtree',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='A lxml helper class to insert element or wrap element to a certain text',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/wbiz/lxmltree',

    # Author details
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