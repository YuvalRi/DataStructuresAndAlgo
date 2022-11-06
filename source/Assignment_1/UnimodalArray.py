import math
# exercise 1, question 2

def unimodal_index(A: list, n: int):
    '''
    A function which returns an index of a given unimodal array.
    Right to the number of this index,
    all elements are smaller and they are sorted in decreasing order.
    Left to number of this index, 
    all elements are smaller and they are sorted in increasing order.
    '''
    found = False
    start = 0
    end = n-1
    if len(A) == 1:
        return 0
    while found == False and start < end:
        mid = math.floor((start+end)/2)
        if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
            found = True
        else:
            if A[mid] > A[mid+1]:
                end = mid - 1
                if A[end] == A[0]:
                    return 0
            else:
                start = mid + 1
                if A[start] == A[n-1]:
                    return n-1
    return mid



