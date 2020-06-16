def peakIndexInMountainArray(A):
    for i in range(len(A)):
        if A[i] > A[i+1]:
            return i
