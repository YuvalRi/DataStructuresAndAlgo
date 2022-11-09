# Merge is a function which called in MergeSort algorithm

def merge(A: list, p: int, q: int, r: int):
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
    i = 0 # initial index of left array (subarray)
    j = 0 # initial index of right array (subarray)
    k = p # initial index of the merged array
    while i < len_1 and j < len_2:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len_1:
        A[k] = left[i]
        i += 1
        k += 1
    while j < len_2:
        A[k] = right[j]
        j += 1
        k += 1