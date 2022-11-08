from BinarySearch_v2 import binary_search2

def find_pivot(A1, start, end):
    '''
    A function which returns a pivot of a rotated array  
    '''
    if end < start:
        return -1 
    if end == start:
        return start
    mid = (start+end)//2
    if mid < end and A1[mid] > A1[mid+1]:
        return mid
    if mid > start and A1[mid] < A1[mid-1]:
        return mid-1 
    if A1[start] >= A1[mid]:
        return find_pivot(A1, start, mid-1)
    return find_pivot(A1, mid+1, end)


def shift_and_sort(A1: list, n: int, val: int):
    '''
    
    '''
    pivot = find_pivot(A1, 0, n-1)
    # the array is not rotated
    if pivot == -1:
        return binary_search2(A1, 0, n-1, val)
    if A1[pivot] == val:
        return pivot
    if A1[0] <= val:
        return binary_search2(A1, 0, pivot-1, val)
    return binary_search2(A1, pivot+1, n-1, val)

