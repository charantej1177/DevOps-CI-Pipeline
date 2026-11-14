from calculator import add, subtract, multiply

# Test addition
def test_add():
    assert add(2, 3) == 5

# Test subtraction
def test_subtract():
    assert subtract(5, 2) == 3

# Test multiplication
def test_multiply():
    assert multiply(4, 3) == 12