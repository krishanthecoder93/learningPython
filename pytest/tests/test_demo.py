from app.demo import *
import pytest
import sys


@pytest.mark.skip(reason="Addition test temporarily disabled")
def test_add():
    assert add(10,20) ==30

@pytest.mark.skipif(sys.version_info<(3,10), reason="Needs Python 3,10+")
def test_sub():
    assert sub(50,20) ==30


def test_mul():
    if sys.platform != "darwin":  # darwin = macOS
        pytest.skip("This test runs only on macOS")
    assert mul(5,6) ==30
    

def test_div():
    assert div(600,20) ==30

    #case  for asserting exceptions
    with pytest.raises(ValueError):
        div(4,0)




