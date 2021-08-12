from calculator import SciCalculator

c = SciCalculator()

def test_sqrt():
    assert c.sqrt(100) == 10
    assert c.sqrt(25) == 5
    # assert c.sqrt(None) == None

def test_floor():
    assert c.floor(13.2) == 13

def test_ceil():
    assert c.ceil(15.8) == 16

