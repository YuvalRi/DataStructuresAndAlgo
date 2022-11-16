# Partition is a function that called in QuickSort algorithm

def partition(A: list, p: int, r: int):
    i = p + 1
    j = r 
    pivot = A[p]
    while i <= j:
        while A[i] < pivot and i < j:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else:
            i += 1
    A[p] = A[j]
    A[j] = pivot
    return j
     
if __name__ == "__main__":
    A = [40, 20, 10, 80, 60, 50, 7, 30, 100]
    print(partition(A, 0, len(A)-1))
    B = [12, 9, 7, 15, 10]
    print(partition(B, 0, len(B)-1))
    C = [9, 2, 55, 76, 24]
    print(partition(C, 0, len(C)-1))


