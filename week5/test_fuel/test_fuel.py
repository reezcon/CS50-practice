from fuel import convert, gauge
import pytest

# Unit tests for convert:

def test_convert_half():
    assert convert("1/2") == 50

def test_convert_full():
    assert convert("1/1") == 100

def test_convert_zero():
    assert convert("0/1") == 0

def test_convert_div_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_improper_fraction():
    with pytest.raises(ValueError):
        convert("7/5")

def test_convert_negativ():
    with pytest.raises(ValueError):
        convert("-1/2")

# Unit tests of gauge:

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(21) == "21%"
