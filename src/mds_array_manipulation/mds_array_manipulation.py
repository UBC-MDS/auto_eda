def search_array(arr, elem):
    """
    Search for elem in a numpy array.
    
    Parameters
    ----------
    arr : numpy.array
        The numpy array to search
    elem : object to search for in the array
    
    Returns
    -------
    int
        Index of the first occurence of the element in the array, -1 if not found
        
    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation.mds_array_manipulation import search_array
    >>> arr = np.array([20, 10, 20, 30, 50, 90, 60])
    >>> search_array(arr, 50)
    4
    >>> search_array(arr, 100)
    -1
    >>> search_array(arr, 20)
    0
    """
    # TODO: actual code
    pass


def count_nonzero_elements(arr):
    """
    Count the number of non zero elements in an array.
    
    Parameters
    ----------
    arr : numpy.array
        The Input array of any dimension (1D, 2D or 3D)
        
    Returns
    -------
    dict : A dictionary containing information about non-zero elements.Below are the keys in the dictionary
      - For 1D array: {'Total Non-Zero Elements in Array': total_nonzero}
      - For 2D or 3D array:
        {
          'Non-Zero Elements in Rows': row_counts,
          'Non-Zero Elements in Columns': col_counts,
          'Total Non-Zero Elements in Array': total_nonzero
        }
        
    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation import mds_array_manipulation as am
    >>> arr = np.array([0, 1, 2])
    >>> am.count_nonzero_elements(arr)
    {'Total Non-Zero Elements in Array': 2}
    >>> arr2d = np.array([[0, 1, 2], [3, 0, 5], [0, 7, 8]])
    >>> am.count_nonzero_elements(arr2d)
        {'Total Non-Zero Elements in Array': 6, 'Non-Zero Elements in Rows': array([2, 2, 2]), 'Non-Zero Elements in Columns': array([1, 2, 3])}
    """
    # TODO: actual code
    pass


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
    >>> import numpy as np
    >>> from mds_array_manipulation.mds_array_manipulation import argmax
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
    # TODO: actual code
    pass

