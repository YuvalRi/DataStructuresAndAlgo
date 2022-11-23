# Partition is a function that called in QuickSort algorithm

def partition(A: list, p: int, r: int):
    i = p
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
    return j, A


if __name__ == "__main__":
    A = [40, 20, 10, 80, 60, 50, 7, 30, 100]
    print(partition(A, 0, len(A)-1))
    B = [12, 9, 7, 15, 10]
    print(partition(B, 0, len(B)-1))
    C = [9, 2, 55, 76, 24]
    print(partition(C, 0, len(C)-1))
    D = [8, 22, 6, 60, 90, 81, 96, 47]
    print(partition(D, 0, len(D)-1))
    E = [5, 1, 6, 3, 2, 4]
    print(partition(E, 0, len(E)-1))

