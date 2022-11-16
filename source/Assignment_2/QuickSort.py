from Partition import partition
# QuickSort algorithm

def quick_sort(A: list, p: int, r: int):
    '''
    A recursive algorithm which sort a given array A
    start index (p), end index (r)
    '''
    if len(A) == 1:
        return A[0]
    if r <= p:
        return
    else:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)
    return A

if __name__ == "__main__":
    A = [40, 20, 10, 80, 60, 50, 7, 30, 100]
    print(quick_sort(A, 0, len(A)-1))
    B = [40, 20, 10]
    print(quick_sort(B, 0, len(B)-1))
    C = [8]
    print(quick_sort(C, 0, len(C)-1))
    D = [8,9,2,5]
    print(quick_sort(D, 5, 3))
    E = [9, 2, 55, 76, 24]
    print(quick_sort(E, 0, len(E)-1))


