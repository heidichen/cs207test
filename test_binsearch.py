from pytest import raises
from binsearch import binary_search

def test_binsearch():
    input = list(range(10))
    assert binary_search(input, 5) == 5

def test_char_binsearch():
    with raises(TypeError):
        binary_search(['a', 3])

def test_binary_empty():
    asset binary_search([], 1) == -1

def test_binary_noitem():
    asset binary_search([3, 4], 1) == -1
