def linearSearch(array, value):
    """ (list, object) -> int
    Returns the index of the first occurance of value in L, or 
    returns -1 is value is not in L
    >>> linearSearch([2, 9, 6, 3, 5], 3)
    3
    >>> linearSearch([1, 0, 4, 5, 0], 0)
    1
    >>> linearSearch([1, 4, 2], 3)
    -1
    >>> linearSearch([], 3)
    -1
    """
    # length of the array
    L = len(array)
    # starting index
    idx = 0
    # loop will continue till the pointer reaches the end
    while idx < L:
        # if a match is found!
        if array[idx] == value:
            return idx
        # increase the pointer if no match is found
        else:
             idx += 1
    # if a match is not found
    return -1

if __name__=='__main__':
    import doctest
    doctest.testmod()
