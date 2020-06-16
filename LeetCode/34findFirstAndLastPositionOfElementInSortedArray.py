def searchRange(nums, target):
    """ (list[int], int) -> list[int]
    Returns the first and last positions of an element in a
    sorted array
    >>> searchRange([5, 7, 7, 8, 8, 8, 10, 11, 12, 15], 8)
    [3, 5]
    >>> searchRange([5,7,7,8,8,10], 8)
    [3, 4]
    >>> searchRange([1], 1)
    [0, 0]
    >>> searchRange([1, 1], 1)
    [0, 1]
    >>> searchRange([5, 7, 7, 8, 8, 8, 10, 11, 12, 15], 13)
    [-1, -1]
    """
    L = len(nums) 
    lowerIdx = 0
    numRange = []

    while lowerIdx < L:
        if nums[lowerIdx] == target:
            numRange.append(lowerIdx)
            nums.reverse()
            targetIdxUp = nums.index(target)  
            numRange.append(L - 1 - targetIdxUp)   
            return numRange
        else:
            lowerIdx +=  1
    return [-1, -1]
if __name__ == '__main__':
    import doctest
    doctest.testmod()
