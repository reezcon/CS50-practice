import pytest
from twttr import shorten

def test_no_vowels():
    assert shorten("gym") == "gym"
    assert shorten("myth") == "myth"

def test_with_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten("cs50") == "cs50"
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
