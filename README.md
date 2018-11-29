[![CircleCI](https://circleci.com/gh/duckietown/duckietown-objdet.svg?style=shield)](https://circleci.com/gh/duckietown/duckietown-objdet)

[![Coverage Status](https://coveralls.io/repos/github/duckietown/duckietown-objdet/badge.svg?branch=master18)](https://coveralls.io/github/duckietown/duckietown-objdet?branch=master18)

[![PyPI status](https://img.shields.io/pypi/status/duckietown_objdet.svg)](https://pypi.python.org/pypi/duckietown_objdet/)


[![PyPI pyversions](https://img.shields.io/pypi/pyversions/duckietown_objdet.svg)](https://pypi.python.org/pypi/duckietown_objdet/)


# objdet

Object detection module challenge for Duckietown


## Installation from source

This is the way to install within a virtual environment created by 
using `pipenv`:

    $ pipenv install
    $ pipenv shell
    $ cd lib-objdet
    $ pip install -r requirements.txt
    $ python setup.py develop --no-deps
    
   
## Unit tests

Run this:

    $ make -C lib-objdet tests-clean tests
    
The output is generated in the folder in `lib-objdet/out-comptests/`.
