# another version of binary search algorithm

def binary_search2(A: list, start: int, end: int, x: int):
    if end < start:
        return -1 
    mid = (start+end)//2
    if x == A[mid]:
        return mid
    elif x > A[mid]:
        return binary_search2(A, mid+1, end, x)
    return binary_search2(A, start, mid-1, x)


if __name__ == "__main__":
    lst1 = [1,2,3,4,5,6]
    print(binary_search2(A = lst1, start=0, end= len(lst1)-1, x = 1))
    print(binary_search2(A = lst1, start=0, end= len(lst1)-1, x = 2))
    print(binary_search2(A = lst1, start=0, end= len(lst1)-1, x = 3))
    print(binary_search2(A = lst1, start=0, end= len(lst1)-1, x = 4))
    print(binary_search2(A = lst1, start=0, end= len(lst1)-1, x = 5))
    print(binary_search2(A = lst1, start=0, end= len(lst1)-1, x = 7))



