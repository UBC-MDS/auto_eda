import pytest
import numpy as np

from mds_array_manipulation.search_array import search_array


#Test with 1D array
def test_1d_search(one_d_int_array):
    ind = search_array(one_d_int_array, 3)
    assert ind == 2
    

def test_1d_search_multiple_match(one_d_int_array):
    ind = search_array(one_d_int_array, 1)
    assert ind == 0

#Test with 2D array
def test_2d_array(two_d_int_array):
    with pytest.raises(ValueError):
        search_array(two_d_int_array, 10)


#Test with element not in array
def test_1d_array_no_match(one_d_int_array):
    ind = search_array(one_d_int_array, 1000)
    assert ind == -1

#Test empty array
def test_1d_array_no_match(empty_array):
    ind = search_array(empty_array, 1)
    assert ind == -1

#Test numeric type
def test_1d_float_array(one_d_float_array):
    ind = search_array(one_d_float_array, 3.14)
    assert ind == 2

#Test string type
def test_1d_string_array(one_d_string_array):
    ind = search_array(one_d_string_array, 'frog')
    assert ind == 4

#Test case sensitive search
def test_1d_string_array(one_d_string_array):
    ind = search_array(one_d_string_array, 'Frog')
    assert ind == -1

#Test tuple
def test_tuple_array():
    tuple_array = np.array([(1,2), (3,4), (5,6)], dtype="i, i")
    with pytest.raises(ValueError):
        search_array(tuple_array, (3,4))
