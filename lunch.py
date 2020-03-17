"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    # print(nrows)
    ncols = len(garden[0])
    # print(ncols)

    current_idx = int() # keeping track of the current position
    carrot_eaten = [] # keeping track of number of carrots then SUM() at the end

    ### TRY: WITH A 3X3 GRID

    # Start at the center of the garden with the most number of carrots
    # find the middle of the grid
    for idx, val in enumerate(garden):
        idx = nrows/2
        current_r_idx = idx

    for idx, val in enumerate(garden):
        idx = ncols/2
        current_c_idx = idx
    # for the idx, val in enumerate(ncols)
    # ncols = ncols/2
    # print(ncols)

    # look to the left of the current_idx (west) keep num of carrots
    # for current_idx in garden:
    for idx, val in enumerate(garden):
        print(current_r_idx - 1, val)
        w_carrot = val
    # look at the above row in current positon (north) keep number of carrots.
    for idx, val in enumerate(garden):
        print((nrow(current_c_idx + 1), val)
        n_carrot = val
    # look to the next index on the same row (east) keep the number of carrots.
    for idx, val in enumerate(garden):
        print(current_r_idx + 1, val)
        e_carrot = val
    # look below onto the next row of the same index position 
    # (south) keep the number of carrots.
    for idx, val in enumerate(garden):
        print((nrow(current_c_idx + 1), val)
        s_carrot = val
    # compare the number of carrots at each direction
    # whichever is the largets move in that direction
    # continue until you reach the end of the garden 

    for carrot in carrot_eaten:
        return sum(carrot)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")






















