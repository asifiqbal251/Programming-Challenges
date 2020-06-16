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
    upperIdx = L  
    
    # find out the target with the lowest index position
    # hence the search includes (greater or equal)
    while lowerIdx < upperIdx:
        targetIdx = (lowerIdx + upperIdx)//2
        # greater or equal
        if nums[targetIdx] >= target:
            upperIdx = targetIdx
        # lower
        else:
            lowerIdx = targetIdx + 1
    
    # find out the target with the highest index position
    # hence the search includes (lower or equal)
    lo = lowerIdx
    upperIdx = L
    while lowerIdx < upperIdx:
        targetIdx = (lowerIdx + upperIdx)//2
        # greater
        if nums[targetIdx] > target:
            upperIdx = targetIdx
        # lower or equal
        else:
            lowerIdx = targetIdx + 1     
            
    if lo == len(nums) or nums[lo] != target:
            return [-1, -1] 
    else:
        return [lo, upperIdx - 1] 
