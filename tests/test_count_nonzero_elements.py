import pytest
import numpy as np
from mds_array_manipulation.mds_array_manipulation import count_nonzero_elements
from conftest import *

#Test for 1D array
def test_1d_array():
    result = count_nonzero_elements(one_d_int_array)
    assert result == {'Total Non-Zero Elements in Array': 7}

#Test for 2D array
def test_2d_array():
    result = count_nonzero_elements(two_d_int_array)
    expected = {'Total Non-Zero Elements in Array': 14, 'Non-Zero Elements in Rows': np.array([7, 7]), 'Non-Zero Elements in Columns': np.array([2, 2, 1, 2, 2, 2, 1, 2])}
    assert result == expected

#Test for 3D array
def test_3d_array():
    result = count_nonzero_elements(three_d_int_array)
    expected = {'Total Non-Zero Elements in Array': 14, 'Non-Zero Elements in Rows': np.array([4, 3, 3, 4]), 'Non-Zero Elements in Columns': np.array([2, 2, 1, 2, 2, 2, 1, 2])}
    assert result == expected

# Test for checking the input data type
def test_input():
    with pytest.raises(ValueError):
        count_nonzero_elements(one_d_string_array, 10)

# Test for all zero elements
def test_all_zeros():
    result = count_nonzero_elements(one_d_int_array_all_zero)
    assert result == {'Total Non-Zero Elements in Array': 0}

# Test for empty array
def test_empty_array():
    result = count_nonzero_elements(empty_array)
    assert result == {'Total Non-Zero Elements in Array': 0}

# Test for floating point numbers which are close to zero - setting tolerance level of 1e-15
def test_floating_point_tolerance():
    result = count_nonzero_elements(one_d_float_tol_array)
    assert result == {'Total Non-Zero Elements in Array': 1}

