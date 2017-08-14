## Synopsis

This repo contains study code that follows the chapters of the book Learning Python 5e.
![book](http://t1.gstatic.com/images?q=tbn:ANd9GcSY2c3h3wIKeR3oqOcvi1qX8BPdRqNrK3o9szUHcre1UyOtFEFP)

Each Chapter directory refers to a chapter of the book and will contain pytest tests that demonstrate specific features of the python language, comparing versions 2.7 and 3.6 whenever appropriate

## Motivation

The motivation behind this repo is to provide an easily referable summation of the concepts laid out in the book.

## Installation

Clone the repository and install tox (http://tox.readthedocs.io/en/latest/example/pytest.html)

## Tests

Tox provides an easy way to test multiple versions of python.

To run the tests of this repo using python 2.7:

tox -e py27

To run with version 3.6:

tox -e py36

To run with both versions:

tox
