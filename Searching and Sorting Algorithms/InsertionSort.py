def insertionSort(array):
    """ (list) -> list
    Returns the sorted list in ascending order
    >>> insertionSort([4, 2, 5, 1, 7])
    [1, 2, 4, 5, 7]
    >>> insertionSort([2, 3, 3])
    [2, 3, 3]
    >>> insertionSort([2])
    [2]
    """
    # length of the array
    L = len(array)   
    # for every pass, we increase end-pointer (1 to L-1) to gradually consider all the elements
    for i in range(1, L):
        # new value to be sorted with the already sorted array
        value = array[i]
        # right pointer to compare/track values
        right = i - 1
        # loop continues if right pointer points an index >= [0] and array[right] > value to be added
        while right >= 0 and array[right] > value:
            # sort and update value if array[right] > value to be added
            array[right + 1] = array[right]
            right -= 1 
        # update and sort value    
        array[right + 1] = value
    return array
if __name__ == '__main__':
    import doctest
    doctest.testmod()            
