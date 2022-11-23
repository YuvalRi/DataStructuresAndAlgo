# count variable added to merger function that used in MergeSort

def merge_count(A: list, p: int, q: int, r: int):
    count = 0
    # length of 2 subarrays:
    # first array is A[p,...q]
    # second array is A[q+1,...r]
    len_1 = q - p + 1
    len_2 = r - q
    # create temp subarrays
    left = [0] * (len_1)
    right = [0] * (len_2)
    # copy current data to left array and right array
    for i in range(0, len_1):
        left[i] = A[p + i]
    for j in range(0, len_2):
        right[j] = A[q+1+j]
    # merge the temp arrays back into our original array - A
    i = 0  # initial index of left array (subarray)
    j = 0  # initial index of right array (subarray)
    k = p  # initial index of the merged array
    while i < len_1 and j < len_2:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            count += 1
            A[k] = right[j]
            j += 1
        k += 1
    while i < len_1:
        count += 1
        A[k] = left[i]
        i += 1
        k += 1
    while j < len_2:
        A[k] = right[j]
        j += 1
        k += 1
    return count


def merge_sort(A: list, p: int, r: int):
    if p < r:
        q = p+(r-p)//2
        c1 = merge_sort(A, p, q)
        c2 = merge_sort(A, q + 1, r)
        c3 = merge_count(A, p, q, r)
        return c1 + c2 + c3

    return 0


if __name__ == "__main__":
    A = [40, 20, 10]
    print(merge_sort(A, 0, len(A)-1))
    B = [1, 7, 9]
    print(merge_sort(B, 0, len(B)-1))
    C = [1, 9, 7]
    print(merge_sort(C, 0, len(C)-1))
    D = [1, 9, 7, 8, 2]
    print(merge_sort(D, 0, len(D)-1))
    E = [1, 2, 3, 4, 5, 6]
    print(merge_sort(E, 0, len(E)-1))
    F = [6, 5, 4, 3, 2]
    print(merge_sort(F, 0, len(F)-1))
    G = [1, 2, 3, 4, 5, 7, 6]
    print(merge_sort(G, 0, len(G)-1))

