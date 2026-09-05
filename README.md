# Object Oriented Programming Lab - Bookstore 

## Description

This project demonstrates object-oriented programming concepts in Python
using `Book` and `Coffee` classes.

## FEATURES

## Book

- Creates a Book object with a title and page count
- Validates that the page count is an integer
- Provides a method to turn a page

## Coffee

- Creates a Coffee object with a size and price
- Validates that the coffee size is Small, Medium, or Large
- Provides a method for adding a tip to the price

## Technologies

- Python 3.8.13

## RUNNING THE TESTS

## Install the project dependencies:

pipenv install

## Activate the virtual environment:

pipenv shell

## Run all test

pytest

## To run the Book tests:

pytest -x testing/book_test.py

## To run the Coffee tests:

pytest -x testing/coffee_test.py