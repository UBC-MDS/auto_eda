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
    >>> from mds_array_manipulation import search_array
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