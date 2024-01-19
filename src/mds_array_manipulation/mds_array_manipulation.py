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


