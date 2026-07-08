from calci import add
import pytest
@pytest.fixture
def a():
    print("calci open")
    print ("10")
    yield
    print("calci close")
'''@pytest.fixture
def b():
    return 20'''
def test_calci(a):
    assert add(5,7)==12
