# Partition is a function that called in QuickSort algorithm

def partition(A: list, p: int, r: int):
    pivot = A[p]
    i = p
    j = r 
    done = False
    while done == False:
        if A[j] > pivot:
            j = j - 1
        if A[i] < pivot:
            i = i + 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            done = True
    print(A)
    return j
     
if __name__ == "__main__":
    A = [40, 20, 10, 80, 60, 50, 7, 30, 100]
    print(partition(A, 0, len(A)-1))
    B = [12, 9, 7, 15, 10]
    print(partition(B, 0, len(B)-1))

