from plates import is_valid
import pytest

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("A") == False
    assert is_valid("CSS5000") == False

def test_starting_2_letters():
    assert is_valid("CS50") == True
    assert is_valid("J21") == False

def test_punctuations():
    assert is_valid("PI3.14") == False
    assert is_valid("HI!") == False
    assert is_valid("HI 08") == False

def test_numbers():
    assert is_valid("YK021") == False # The first number cannot be 0
    assert is_valid("AE76A") == False # Numbers must come at the end

