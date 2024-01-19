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
    i = 0 
    while i < len(arr):
        if arr[i] == elem:
            return i
    return -1
    


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


