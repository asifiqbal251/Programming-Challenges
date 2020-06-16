def binarySearch(array, value):
    """ (list, object) -> int
    Precondition: L is sorted from smallest to largest, and
    all the items in L can be compared to v.
    
    Returns the index of the first occurance of v in L, or 
    returns -1 is v is not in L
    >>> binarySearch([-1, 2, 3, 6, 20, 50], 3)
    2
    >>> binarySearch([0, 1, 4, 5, 7], 0)
    0
    >>> binarySearch([1, 2, 4], 3)
    -1
    >>> binarySearch([], 3)
    -1
    
    """
    # length of the array
    L = len(array)
    # position of the start-pointer
    start = 0
    # position of the end-pointer
    end = L - 1
    
    # loop will continue till start-pointer crosses the end-pointer
    while start <= end: 
        # value at the mid point (index is floored)
        midIdx = (start + end)//2
        
        # if a match is found! 
        if array[midIdx] == value:
            return midIdx
        # shifing the start-pointer
        elif array[midIdx] < value:
            start = midIdx + 1
        # shifting the end-pointer    
        else:
            end = midIdx - 1
    # if a match is not found from the search        
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod() 
