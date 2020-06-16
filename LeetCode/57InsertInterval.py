def insertInterval(intervals, newInterval):
    """ (list[list[int]], list[int]) -> list[list[int]]
    >>> insertInterval([[1, 3], [6, 9]], [2, 5])
    [[1, 5], [6, 9]]
    >>> insertInterval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    [[1, 2], [3, 10], [12, 16]]
    >>> insertInterval([], [5, 7])
    [[5, 7]]
    >>> insertInterval([[1,5]], [2,3])
    [[1, 5]]
    """
    L = len(intervals)
    combinedInterval = []
    intIdx = 0
    start = newInterval[0]
    end = newInterval[1]
    
    # append intervals that starts before the new interval
    while intIdx < L and intervals[intIdx][0] < start:
        combinedInterval.append(intervals[intIdx])
        intIdx += 1
    # modify the entry with the new interval  
    # if empty combinedInterval or the new interval starts later than the combinedinterval, add the interval
    if not combinedInterval or combinedInterval[-1][1] < start:  
        combinedInterval.append(newInterval)
    # else the new interval overlaps with the existing combinedInterval, start is already merged with the
    # existing combinedInterval. Only need to choose the end point of the new interval added.
    else:
        combinedInterval[-1][1] = max(combinedInterval[-1][1], end)
        
    # add the rest of the intervals with appropriate merging             
    while intIdx < L:
        interval = intervals[intIdx]
        start, end = interval[0], interval[1]
        intIdx += 1
        # if no overlap, simply add the new interval
        if combinedInterval[-1][1] < start:
            combinedInterval.append(interval)
        # if overlap exists, add the new interval appropriately    
        else:
            combinedInterval[-1][1] = max(combinedInterval[-1][1], end)
    return combinedInterval
if __name__ == '__main__':
    import doctest
    doctest.testmod()
