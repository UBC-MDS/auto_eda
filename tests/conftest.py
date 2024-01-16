import pytest
import numpy as np

@pytest.fixture
def empty_array():
    return np.array([])

@pytest.fixture
def one_d_int_array():
    return np.array([1,5,3,9,18,24,0,1])

@pytest.fixture
def one_d_int_array_one_element():
    return np.array([5])

@pytest.fixture
def one_d_int_array_all_zero():
    return np.array([0,0,0,0,0,0])

@pytest.fixture
def one_d_float_array():
    return np.array([1.0,5.1,3.14,9.62,18.88,24.01,0.0,1.5])

@pytest.fixture
def one_d_neg_array():
    return np.array([1,5,-3,9,-18,24,0,-1])

@pytest.fixture
def one_d_string_array():
    return np.array(['dog', 'cat', 'banana', 'apple', 'frog'])

@pytest.fixture
def two_d_int_array():
    return np.array([[1,5,3,9,18,24,0,1], [10,1,0,25,-1,-200,4,33]])

@pytest.fixture
def two_d_float_array():
    return np.array([1.0,5.1,3.14,9.62,18.88,24.01,0.0,1.5], \
                    [10.0,1.01,0.01,25.67,-1.4444,-200.2,4.8,33.3])

@pytest.fixture
def two_d_string_array():
    return np.array(['dog', 'cat', 'banana', 'apple', 'frog'], \
                    ['elephant', 'soup', 'aardvark', 'mouse', 'power'])

@pytest.fixture
def three_d_int_array():
    return np.array([[[1,5,3,9],[18,24,0,1]], [[10,1,0,25],[-1,-200,4,33]]])

