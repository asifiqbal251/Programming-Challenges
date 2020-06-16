def isAsc(nums):
    """ (list) -> bool
    Returns if an array is sorted in ascending order
    >>> isAsc([-1, 2, 3, 6, 20, 50])
    True
    >>> isAsc([-1, 2, 3, 6, 20, 50, -1])
    False
    >>> isAsc([-1])
    True
    """
    L = len(nums)
    for i in range(L - 1):
        if nums[i + 1] < nums[i]:
            return False
        else:
            continue
    return True


def isSorted(nums):
    """ (list) -> bool
    Returns if an array is sorted in ascending/descending order
    >>> isSorted([-1, 2, 3, 6, 20, 50])
    True
    >>> isSorted([-1, 2, 3, 6, 20, 50, -1])
    False
    >>> isSorted([-1])
    True
    >>> isSorted([1, 2])
    True
    >>> isSorted([2, 1, -9, -100])
    True
    """
    L = len(nums)
    if isAsc(nums) == True or isAsc(nums[::-1]) == True:
        return True
    else:
        return False
    
if __name__ == '__main__':
    import doctest
    doctest.testmod() 
