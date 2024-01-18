from mds_array_manipulation import mds_array_manipulation as am
import numpy as np
import pytest

# The following test is for the function sort_array

# checks if a ValueError is raised for non-1D arrays
def test_input_not_1d_array_1(two_d_int_array):
    with pytest.raises(ValueError):
        am.sort_array(two_d_int_array)

def test_input_not_1d_array_2(three_d_int_array):
    with pytest.raises(ValueError):
        am.sort_array(three_d_int_array)

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
            am.sort_array(input)

# checks if a single-element array is returned as is
def test_single_element_array_1(one_d_int_array_one_element):
    result = am.sort_array(one_d_int_array_one_element)
    assert np.array_equal(result, one_d_int_array_one_element)

def test_single_element_array_2(one_d_string_array_one_element):
    result = am.sort_array(one_d_string_array_one_element)
    assert np.array_equal(result, one_d_string_array_one_element)

# checks if an empty array is returned as is
def test_empty_array(empty_array):
    result = am.sort_array(empty_array)
    assert np.array_equal(result, empty_array)

# checks if the function can sort arrays of integers and floats
def test_sorts_numeric_types(one_d_int_array, one_d_float_array):
    assert np.array_equal(am.sort_array(one_d_int_array), np.array(sorted(one_d_int_array)))
    assert np.array_equal(am.sort_array(one_d_float_array), np.array(sorted(one_d_float_array)))

# checks if the function can sort arrays of strings
def test_sorts_numeric_types(one_d_string_array):
    result = am.sort_array(one_d_string_array)
    assert np.array_equal(result, np.array(sorted(one_d_string_array)))  

# checks if a TypeError is raised for arrays with mixed data types
def test_input_different_type():
    with pytest.raises(TypeError):
        am.sort_array(['a', 1, 'b', 2])

# checks if the function can sort arrays with negative numbers
def test_negative_input(one_d_neg_array):
    result = am.sort_array(one_d_neg_array)
    assert np.array_equal(result, np.array(sorted(one_d_neg_array)))

# checks if the function can sort a mixed-case string array in a case-insensitive manner
def test_lowercase_uppercase_strings(one_d_string_array_mixed_case):
    result = am.sort_array(one_d_string_array_mixed_case)
    assert np.array_equal(result, np.array(sorted(one_d_string_array_mixed_case, key=str.lower)))

# checks if a sorted array remains unchanged after sorting again
def test_already_sorted_array(one_d_int_array_sorted):
    result = am.sort_array(one_d_int_array_sorted)
    assert np.array_equal(result, one_d_int_array_sorted)