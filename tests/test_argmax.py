import pytest
import numpy as np
from mds_array_manipulation.argmax import argmax


# Test case for a valid 1D integer array
def test_argmax_1d_int_array(one_d_int_array):
    result = argmax(one_d_int_array)
    assert result == 5  

# Test case for a 1D integer array with one element
def test_argmax_1d_int_array_one_element(one_d_int_array_one_element):
    result = argmax(one_d_int_array_one_element)
    assert result == 0  

# Test case for a 1D integer array with all zero elements
def test_argmax_1d_int_array_all_zero(one_d_int_array_all_zero):
    result = argmax(one_d_int_array_all_zero)
    assert result == 0  

# Test case for a 1D float array
def test_argmax_1d_float_array(one_d_float_array):
    result = argmax(one_d_float_array)
    assert result == 5  

# Test case for a 1D float array with elements close to zero
def test_argmax_1d_float_tol_array(one_d_float_tol_array):
    result = argmax(one_d_float_tol_array)
    assert result == 1  

# Test case for a 1D negative integer array
def test_argmax_1d_neg_array(one_d_neg_array):
    result = argmax(one_d_neg_array)
    assert result == 5  

# Test case for a 1D string array
def test_argmax_1d_string_array(one_d_string_array):
    result = argmax(one_d_string_array)
    assert result == 4

# Test case for a valid 2D integer array with axis=0
def test_argmax_2d_int_array_axis_0(two_d_int_array):
    result = argmax(two_d_int_array, axis=0)
    assert result == [5, 7]  

# Test case for a valid 2D float array with axis=1
def test_argmax_2d_float_array_axis_1(two_d_float_array):
    result = argmax(two_d_float_array, axis=1)
    assert result == [1, 0, 0, 1, 0, 0, 1, 1]  

# Test case for an invalid 2D string array with axis=None
def test_argmax_2d_string_array_axis_none(two_d_string_array):
    result = argmax(two_d_string_array, axis=None)
    assert result == 6

# Test case for a valid 3D integer array
def test_argmax_3d_int_array(three_d_int_array):
    result = argmax(three_d_int_array)
    assert result == 15

# Test case for a empty array
def test_argmax_empty_array(empty_array):
    with pytest.raises(ValueError, match="Input array is an empty array. Please do not enter an empty array."):
        argmax(empty_array) 

# Test case for a 1D array with axis=1
def test_argmax_1d_array_axis_1(one_d_int_array):
    with pytest.raises(ValueError, match="Cannot enter a 1D numpy array with axis = 1. Please enter again."):
        argmax(one_d_int_array, axis=1)

# Test case for axis not 0 or 1
def test_argmax_1d_array_axis_2(one_d_int_array):
    with pytest.raises(ValueError, match="Error caused by axis specified other than 0 or 1."):
        argmax(one_d_int_array, axis=2)

# Test case for none numpy array
def test_argmax_none_numpy_array(none_numpy_array):
    with pytest.raises(ValueError, match="Input array is not a numpy array. Please enter only numpy array."):
        argmax(none_numpy_array)
