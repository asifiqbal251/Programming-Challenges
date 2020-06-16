def mergeSort(array):
    """ (list) -> list
    Returns the sorted list in ascending order
    >>> mergeSort([12, 3, -4, 21, 0, 200, 22, 44, 19, 0, -3 , 5])
    [-4, -3, 0, 0, 3, 5, 12, 19, 21, 22, 44, 200]
    >>> mergeSort([2, 3, 4, 1, 0, 2])
    [0, 1, 2, 2, 3, 4]
    >>> mergeSort([2, 3])
    [2, 3]
    >>> mergeSort([3, 2, 1])
    [1, 2, 3]
    >>> mergeSort([2, 2, 2])
    [2, 2, 2]
    """
    # length of the array
    L = len(array)
    if L > 1:
        # middle point
        midIdx = L//2
        # left portion
        leftArray = array[: midIdx]
        # right portion
        rightArray = array[midIdx:]
        
        # recursivly call left and right partitions till there's nothing to divide
        mergeSort(leftArray)
        mergeSort(rightArray)
        
        # starting index of the left partition
        leftIdx = 0
        # starting index of the right partition
        rightIdx = 0
        # index of the original array
        arrayIdx = 0
        
        # loop compares and sorts values in two partitions
        while leftIdx < len(leftArray) and rightIdx < len(rightArray):
            # when the smallest value is found in left array
            if leftArray[leftIdx] < rightArray[rightIdx]:
                array[arrayIdx] = leftArray[leftIdx]
                # advance the left array index
                leftIdx += 1
            # when the smallest value is found in right array    
            else:
                array[arrayIdx] = rightArray[rightIdx]
                # advance the right array index
                rightIdx += 1
            # advance the original array index   
            arrayIdx += 1
        
        # if left array still contains value after the comparison
        while leftIdx < len(leftArray):
            array[arrayIdx] = leftArray[leftIdx]
            leftIdx += 1
            arrayIdx +=1
        # if right array still contains value after the comparison    
        while rightIdx < len(rightArray):
            array[arrayIdx] = rightArray[rightIdx]
            rightIdx += 1
            arrayIdx +=1      
    return array

if __name__ == '__main__':
    import doctest
    doctest.testmod() 
