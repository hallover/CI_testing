import pytest
from demo.trial import square

def test_square():

    assert 9==square(3)
    assert 0==square(0)
