import pytest
from app import Calculator

# Fixture to create an instance of the Calculator class
@pytest.fixture
def calculator():
    return Calculator()

# Test case for the add method
def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    assert calculator.add(-5, -7) == -12


# Test case for the div method
##def test_div(calculator):
 ##   assert calculator.div(4, 2) == 2
 ##   assert calculator.div(-1, 1) == -1
   # assert calculator.div(0, 5) == 0

# Test case for division by zero
#def test_div_by_zero(calculator):
  #  with pytest.raises(ValueError):
  #      calculator.div(10, 0)