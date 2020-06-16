def merge(intervals):
    """ (list(list(int, int))) -> list(list(int, int))
    Returns the new intervals with merging
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1,4],[0,2],[3,5]])
    [[0, 5]]
    >>> merge([[1,4],[4,5]])
    [[1, 5]]
    >>> merge([[1,4],[4,5]])
    [[1, 5]]
    >>> merge([[1,4],[2,3]])
    [[1, 4]]
    >>> merge([[1,2],[4,6]])
    [[1, 2], [4, 6]]
    """
    # length of the list of the intervals 
    L = len(intervals)
    # sort the interval according to the start values of the intervals
    intervals.sort(key = lambda value: value[0])
    # to store the merged interval
    mergedInt = []
    # loop continues till all the intervals are considered
    for interval in intervals:
        # if an empty interval or no merge is found between intervals (merge[-1][1] < interval[0]), 
        # simply append the interval
        if not mergedInt or mergedInt[-1][1] < interval[0]:
            mergedInt.append(interval)
        # else a merge is possible, and the merged interval will be merged[-1][0] and 
        # max of merged[-1][1] and interval[1]
        else:
            mergedInt[-1][1] = max(mergedInt[-1][1], interval[1])
    return mergedInt
if __name__ == '__main__':
    import doctest
    doctest.testmod()
