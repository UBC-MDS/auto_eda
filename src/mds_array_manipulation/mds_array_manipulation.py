def argmax(arr, axis=None):
    """
    Returns the indices of the maximum values along an axis from given array.

    Parameters
    ----------
    arr : numpy.array
        Input array.
    axis : int, optional
        Axis along which to operate. By default, flattened input is used.

    Returns
    -------
    indices : int or tuple of ints
        Indices of the maximum values along the specified axis.

    Notes
    -----
    If there are multiple occurrences of the maximum values, the indices
    corresponding to the first occurrence are returned.

    Examples
    --------
    >>> a = np.arange(6).reshape(2,3)
    >>> a
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> argmax(a)
    5
    >>> argmax(a, axis=0)
    array([1, 1, 1])
    >>> argmax(a, axis=1)
    array([2, 2])

    >>> b = np.arange(6)
    >>> b[1] = 5
    >>> b
    array([0, 5, 2, 3, 4, 5])
    >>> argmax(b)  # Only the first occurrence is returned.
    1
    """
    array = np.array(arr)  # Convert input to a NumPy array, in case of input array is not numpy array 
    if axis is None:
        # Flatten the array if no axis is specified
        flattened_array = array.flatten()
        max_value = None
        max_index = None
        for i, value in enumerate(flattened_array):
            if max_value is None or value > max_value:
                max_value = value
                max_index = i
        return max_index
    else:
        # Find the maximum along the specified axis
        max_values = [None] * array.shape[axis]
        max_indices = [None] * array.shape[axis]
        if axis == 0:
            for i in range(array.shape[axis]):
                for j in range(array.shape[1]):
                    if max_values[i] is None or array[i, j] > max_values[i]:
                        max_values[i] = array[i, j]
                        max_indices[i] = j
        elif axis == 1:
            for j in range(array.shape[axis]):
                for i in range(array.shape[0]):
                    if max_values[j] is None or array[i, j] > max_values[j]:
                        max_values[j] = array[i, j]
                        max_indices[j] = i
        return max_indices


def sort_array(arr):
    """
    Sort a numpy array in ascending or alphabetical order.

    Parameters
    ----------
    arr : numpy.array
        The numpy array to be sorted. The array can contain numerical 
        or string values.

    Returns
    -------
    numpy.array
        A new numpy array sorted in ascending or alphabetical order.

    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation import mds_array_manipulation as am
    >>> arr = np.array([20, 10, 40, 30, 50, 90, 60])
    >>> sort_array(arr)
    array([10, 20, 30, 40, 50, 60, 90])

    >>> arr_str = np.array(["orange", "grape", "apple"])
    >>> sort_array(arr_str)
    array(['apple', 'grape', 'orange'])
    """
    # TODO: actual code
    pass