import math

def shift_and_sort(A1: list, n: int, val: int):
    found = False
    start = 0
    end = n-1
    while found == False and start <= end:
        mid = math.floor((start+end)/2)
        if A1[mid] == val:
            found = True
        elif val < A1[start]:
            start = mid + 1
            if val == A1[end]:
                return end
        elif val >= A1[start]:
            end = mid - 1
            if val == A1[end]:
                return end
    if found:
        return mid
    return -1        

            

