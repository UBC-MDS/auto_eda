import pytest
import numpy as np
from mds_array_manipulation.sort_array import sort_array

# The following tests are for the function sort_array

# checks if a ValueError is raised for non-1D arrays
def test_input_not_1d_array_1(two_d_int_array):
    with pytest.raises(ValueError):
        sort_array(two_d_int_array)

#Tests if the function raises an error if the input array is greater than 1D
def test_input_not_1d_array_2(three_d_int_array):
    with pytest.raises(ValueError):
        sort_array(three_d_int_array)

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
            sort_array(input)

# checks if a single-element array is returned as is
def test_single_element_array_1(one_d_int_array_one_element):
    result = sort_array(one_d_int_array_one_element)
    assert np.array_equal(result, one_d_int_array_one_element)

def test_single_element_array_2(one_d_string_array_one_element):
    result = sort_array(one_d_string_array_one_element)
    assert np.array_equal(result, one_d_string_array_one_element)

# checks if an empty array is returned as is
def test_empty_array(empty_array):
    result = sort_array(empty_array)
    assert np.array_equal(result, empty_array)

# checks if the function can sort arrays of integers and floats
def test_sorts_numeric_types(one_d_int_array, one_d_float_array):
    assert np.array_equal(sort_array(one_d_int_array), np.array([0, 1, 1, 3, 5, 9, 18, 24]))
    assert np.array_equal(sort_array(one_d_float_array), np.array([0.0, 1.0, 1.5, 3.14, 5.1, 9.62, 18.88, 24.01]))

# checks if the function can sort arrays of strings
def test_sorts_string_types(one_d_string_array):
    result = sort_array(one_d_string_array)
    assert np.array_equal(result, np.array(['apple', 'banana', 'cat', 'dog', 'frog']))  

# checks if a TypeError is raised for arrays with mixed data types
def test_input_different_type():
    with pytest.raises(TypeError):
        sort_array(['a', 1, 'b', 2])

# checks if the function can sort arrays with negative numbers
def test_negative_input(one_d_neg_array):
    result = sort_array(one_d_neg_array)
    assert np.array_equal(result, np.array([-18, -3, -1, 0, 1, 5, 9, 24]))

# checks if the function can sort a mixed-case string array in a case-insensitive manner
def test_lowercase_uppercase_strings(one_d_string_array_mixed_case):
    result = sort_array(one_d_string_array_mixed_case)
    assert np.array_equal(result, np.array(['apple', 'Banana', 'cat', 'Dog', 'Frog']))

# checks if a sorted array remains unchanged after sorting again
def test_already_sorted_array(one_d_int_array_sorted):
    result = sort_array(one_d_int_array_sorted)
    assert np.array_equal(result, one_d_int_array_sorted)