def bubbleSort(array):
    """ (list) -> list
    Returns the sorted list in ascending order
    >>> bubbleSort([2, 3, 4, 1, 0, 2])
    [0, 1, 2, 2, 3, 4]
    >>> bubbleSort([2, 3])
    [2, 3]
    >>> bubbleSort([3, 2, 1])
    [1, 2, 3]
    >>> bubbleSort([2, 2, 2])
    [2, 2, 2]
    """
    # length of the array
    L = len(array)
    # index of the last element
    end = L -1
    # loop continues till the index of the last elment is 0, as we compare values at [1] and [0]
    while end > 0:
        # finding max for each pass
        for i in range(end):
            # swap values if the left value > right value
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]   
        end -= 1      
    return array

if __name__ == '__main__':
    import doctest
    doctest.testmod()    
