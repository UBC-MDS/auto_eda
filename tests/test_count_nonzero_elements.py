import pytest
import numpy as np
from mds_array_manipulation.count_nonzero_elements import count_nonzero_elements

#Test for 1D array
def test_1d_array(one_d_int_array):
    result = count_nonzero_elements(one_d_int_array)
    assert result == {'Total Non-Zero Elements in Array': 7}

#Test for 2D array
def test_2d_array(two_d_int_array):
    result = count_nonzero_elements(two_d_int_array)
    print(type(result))
    expected = {'Total Non-Zero Elements in Array': 14, 'Non-Zero Elements in Rows': np.array([7, 7]), 'Non-Zero Elements in Columns': np.array([2, 2, 1, 2, 2, 2, 1, 2])}
    print(type(expected))
    for key, value in expected.items():
        assert np.array_equal(result[key], value)

#Test for 3D array
def test_3d_array(three_d_int_array):
    result = count_nonzero_elements(three_d_int_array)
    expected = {'Total Non-Zero Elements in Array': 14, 'Non-Zero Elements in Rows': np.array([4, 3, 3, 4]), 'Non-Zero Elements in Columns': np.array([2, 2, 1, 2, 2, 2, 1, 2])}
    for key, value in expected.items():
        assert np.array_equal(result[key], value)

# checks if the function correctly handles inputs that are not numpy arrays
def test_input_not_numpy_array():
    non_numpy_inputs = [
        [1, 2, 3],
        (1, 2, 3),
        100,
        "not a numpy array",
    ]
    for input in non_numpy_inputs:
        with pytest.raises(TypeError):
            count_nonzero_elements(input)

# Test for checking the input data type
def test_input(one_d_string_array):
    with pytest.raises(ValueError):
        count_nonzero_elements(one_d_string_array)

# Test for all zero elements
def test_all_zeros(one_d_int_array_all_zero):
    result = count_nonzero_elements(one_d_int_array_all_zero)
    assert result == {'Total Non-Zero Elements in Array': 0}

# Test for empty array
def test_empty_array(empty_array):
    result = count_nonzero_elements(empty_array)
    assert result == {'Total Non-Zero Elements in Array': 0}

# Test for floating point numbers which are close to zero - setting tolerance level of 1e-15
def test_floating_point_tolerance(one_d_float_tol_array):
    result = count_nonzero_elements(one_d_float_tol_array)
    assert result == {'Total Non-Zero Elements in Array': 1}

