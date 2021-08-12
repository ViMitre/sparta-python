import pytest
from scrabble import *

s = Scrabble(10)

# Same as below
@pytest.mark.parametrize("testword, expected_score",
                         [
                             ('elephant', 13),
                             ('happy', 15),
                             ('fog', 7),
                             ('frog', 8)
                         ])
def test_return_score(testword, expected_score):
    assert s.return_score(testword) == expected_score

# def test_return_score():
#     assert s.return_score('elephant') == 13
#     assert s.return_score('happy') == 15
#     assert s.return_score('fog') == 7
#     assert s.return_score('frog') == 8
