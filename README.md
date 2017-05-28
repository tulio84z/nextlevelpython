## Synopsis

This repo contains study code that follows the chapters of the book Learning Python 5e. 
## Code Example

Each Chapter directory refers to a chapter of the book and will contains pytest tests that demonstrate features of the python language

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