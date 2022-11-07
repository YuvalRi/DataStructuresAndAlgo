import math

def shift_and_sort(A1: list, n: int, val: int):
    start = 0
    end = n-1
    mid = math.floor((start+end)/2)
    while start - end > 1:
        if A1[mid] <= A1[end]:
            end = mid
        else:
            start = mid
        
    if found:
        return mid
    return -1        

            

