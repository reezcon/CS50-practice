from bank import value
import pytest

def test_hello():
    assert value("hello") == 0

def test_hello_caps():
    assert value("HELLO") == 0

def test_starting_h():
    assert value("hi") == 20
    assert value("hey") == 20
