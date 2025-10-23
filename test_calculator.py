import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    result = add(5, 7)
    assert result == 12 

def test_add_negative_numbers():
    result = add(-4, -6)
    assert result == -10

def test_subtract_positive_numbers():
    result = subtract(10, 4) 
    assert result == 6     

def test_subtract_larger_from_smaller():
    result = subtract(5, 12)
    assert result == -7

def test_multiply_positive_numbers():
    result = multiply(6, 7)
    assert result == 42

def test_multiply_by_zero():
    result = multiply(8, 0)
    assert result == 0      

def test_divide_positive_numbers():
    result = divide(20, 5)  
    assert result == 4      

def test_divide_by_one():
    result = divide(15, 1)  
    assert result == 15

def test_divide_by_zero():
    result = divide(10, 0)  
    assert result == "I dont think you can do that smart guy"  # Expected result based on your implementation



