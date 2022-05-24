import pytest
from ch02variables.lesson18functionsReturningValues import *

def test_add():
    assert add(3, 5) == 8, "addition test"

def test_divide():
    assert divide(15, 3) == 5,              "happy path"
    assert divide(15, 0) == "You fool!",    "check for divide by zero"

def test_return_42():
    assert return_42() == 42, "returns correct value, the answer to everything"

def test_my_function():
    assert my_function(2, 5) == 10, "positive numbers"
    assert my_function(0, 20) == 0, "multiply by zero"
