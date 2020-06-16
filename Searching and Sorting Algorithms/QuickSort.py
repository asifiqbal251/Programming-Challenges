def quickSort(array, start, end):
    """(list, int, int) -> list
    Returns the sorted list in ascending order
    >>> quickSort([20, 6, 8, 53, 56, 23, 87, 41, 49, 19], 0, len([20, 6, 8, 53, 56, 23, 87, 41, 49, 19]) - 1)
    [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
    >>> quickSort([1, 2, 3, 4], 0, len([1, 2, 3, 4])-1)
    [1, 2, 3, 4]
    """
    
    if start < end:
        # index of the pivot value
        pivotIdx = partition(array, start, end)
        # calling quickSort for left and right partitions of the pivot value
        quickSort(array, start, pivotIdx - 1)
        quickSort(array, pivotIdx + 1, end)
    return array    
def partition(nums, start, end):
    # select the first value as the pivot value
    pivotValue = nums[start]
    # lower index
    lowerIdx = start + 1
    # upper index
    upperIdx = end
    
    # search for the cross-over point
    done = False
    while not done:
        # increase lower index if
        while lowerIdx <= upperIdx and nums[lowerIdx] <= pivotValue:
            lowerIdx += 1
        # decrease upper index if
        while upperIdx >= lowerIdx and nums[upperIdx] >= pivotValue:
            upperIdx -= 1
        
        # if two indices cross, we have the crossover point
        if upperIdx < lowerIdx:
            done = True
        else:
            #exchange the two values
            nums[lowerIdx], nums[upperIdx] = nums[upperIdx], nums[lowerIdx]
    # if crossover point is found, exchange the pivot value        
    nums[start], nums[upperIdx] = nums[upperIdx], nums[start]
    return upperIdx
if __name__ == '__main__':
    import doctest
    doctest.testmod() 
