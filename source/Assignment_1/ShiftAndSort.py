from BinarySearch import binary_search

def shift_and_sort(A1: list, n: int, val: int):
    start = 0
    end = n-1
    mid = (start+end)//2
    if start <= end:
        if A1[mid] <= A1[end]:
            end = mid
        else:
            start = mid + 1
    index1 = binary_search(len(A1), A1, val)
    index2 = binary_search(len(A1), A1, val)
    if index1 != -1:
        return index1
    elif index2 != -1:
        return index2
    return -1 
             
if __name__ == "__main__":
    lst2 = [4,5,6,1,2,3]
    print(shift_and_sort(A1=lst2, n=len(lst2),val = lst2[0]))
    print(shift_and_sort(A1=lst2, n=len(lst2),val = lst2[1]))
    print(shift_and_sort(A1=lst2, n=len(lst2),val = lst2[2]))
    print(shift_and_sort(A1=lst2, n=len(lst2),val = lst2[3]))
    print(shift_and_sort(A1=lst2, n=len(lst2),val = lst2[4]))
    print(shift_and_sort(A1=lst2, n=len(lst2),val = lst2[5]))