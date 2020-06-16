def findMedianSortedArrays(nums1, nums2):
    """ (list[int], list[int] -> float)
    Returns the median of the two sorted arrays.
    """
    # length of the arrays
    L1 = len(nums1)
    L2 = len(nums2)
    # construct the combined array
    combinedArray = [0]*(L1 + L2)

    # pointer for first array
    pointer1 = 0
    # pointer for second array
    pointer2 = 0
    # pointer for combined array
    arrayIdx = 0
    
    # algorithm similar to merge sort
    while pointer1 < L1 and pointer2 < L2:
        if nums1[pointer1] < nums2[pointer2]:
            combinedArray[arrayIdx] = nums1[pointer1]
            pointer1 += 1
        else:
            combinedArray[arrayIdx] = nums2[pointer2]
            pointer2 += 1  
        arrayIdx += 1
    while pointer1 < L1:
        combinedArray[arrayIdx] = nums1[pointer1]
        pointer1 += 1
        arrayIdx += 1
    while pointer2 < L2:
        combinedArray[arrayIdx] = nums2[pointer2]
        pointer2 += 1
        arrayIdx += 1

    if (L1 + L2)%2 != 0:
        return combinedArray[(L1 + L2)//2]
    else:
        return (combinedArray[(L1 + L2)//2] + combinedArray[(L1 + L2)//2 - 1])/2
