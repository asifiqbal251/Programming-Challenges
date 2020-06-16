def selectionSort(array):
    """ (list) -> list
    Returns the sorted list in ascending order
    >>> selectionSort([4, 2, 5, 1, 7])
    [1, 2, 4, 5, 7]
    >>> selectionSort([2, 3, 3])
    [2, 3, 3]
    >>> selectionSort([2])
    [2]
    """
    # length of the array
    L = len(array)
    # starting index to hold the minimum of each pass
    start = 0
    # loop continues till starting index = L -1 (end index)
    while (start < L - 1):
        # index of the minimum value
        minIdx = start
        for i in range(start + 1, L):
            if array[minIdx] > array[i]:
                minIdx = i
                
        # swap min value with the value at the starting index
        array[start], array[minIdx] = array[minIdx], array[start]  
        
        start += 1
    return array
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
