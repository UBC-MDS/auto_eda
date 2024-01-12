# mds_array_manipulation

It will do array manipulations functions like Searching, Sorting, Counting non-zero elements, Finding indices of max value. This is a package developed for the group-17 project for the UBC MDS DSCI 524 (Collaborative Software Development) course.

## Installation

```bash
$ pip install mds_array_manipulation
```

## Features

Contains functions: Searching, Sorting, Counting non-zero elements, Finding indices of max value. This package is a group-17 project for the UBC MDS DSCI 524 (Collaborative Software Development) course.

## Dependencies

- Python 3 or greater

## Usage

Example usage:
```bash
>>> import numpy as np
>>> from mds_array_manipulation.mds_array_manipulation import search_array, argmax, sort_array, count_nonzero_elements 
>>> arr = np.array([20, 10, 40, 30, 50, 90, 60])
>>> search_array(arr, 50)
    4
>>> argmax(arr)
    5
>>> sort_array(arr)
    array([10, 20, 30, 40, 50, 60, 90])
>>> count_nonzero_elements(arr)
    7
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`mds_array_manipulation` was created by Kittipong Wongwipasamitkun, Sean Mckay, Yan Zeng, Aishwarya Nadimpally. It is licensed under the terms of the MIT license.

## Credits

`mds_array_manipulation` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
