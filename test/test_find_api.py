import pytest
from crylib import find_api

def test_basic():
    results = find_api(b'xxxxxxxxxhelloxxxxxxworldxxxx', {'test.dll': ['hello', 'world']})
    assert(len(results) == 1)
    assert(len(results[0]['functions']) == 2)
