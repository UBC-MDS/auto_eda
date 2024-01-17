import pytest
import numpy as np
from mds_array_manipulation.mds_array_manipulation import search_array 


one_d_int_array = np.array([1,5,3,9,18,24,0,1])
empty_array = np.array([])
one_d_float_array = np.array([1.0,5.1,3.14,9.62,18.88,24.01,0.0,1.5])
one_d_string_array = np.array(['dog', 'cat', 'banana', 'apple', 'frog'])
two_d_int_array = np.array([[1,5,3,9,18,24,0,1], [10,1,0,25,-1,-200,4,33]])

#Test with 1D array
def test_1d_search():
    ind = search_array(one_d_int_array, 3)
    assert ind == 2
    

def test_1d_search_multiple_match():
    ind = search_array(one_d_int_array, 1)
    assert ind == 0

#Test with 2D array
def test_2d_array():
    with pytest.raises(ValueError):
        search_array(two_d_int_array, 10)


#Test with element not in array
def test_1d_array_no_match():
    ind = search_array(one_d_int_array, 1000)
    assert ind == -1

#Test empty array
def test_1d_array_no_match():
    ind = search_array(empty_array, 1)
    assert ind == -1

#Test numeric type
def test_1d_float_array():
    ind = search_array(one_d_float_array, 3.14)
    assert ind == 2

#Test string type
def test_1d_string_array():
    ind = search_array(one_d_string_array, 'frog')
    assert ind == 4

#Test case sensitive search
def test_1d_string_array():
    ind = search_array(one_d_string_array, 'Frog')
    assert ind == -1

#Test tuple
def test_tuple_array():
    tuple_array = np.array([(1,2), (3,4), (5,6)])
    with pytest.raises(ValueError):
        search_array(tuple_array, (3,4))

