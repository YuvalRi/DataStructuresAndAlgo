# This algorithm is a variation of 'partition' procedure used in Quick Sort.


def one_zero_array(A: list):
    '''
    The function receives an array of only {0,1} elements
    and sorts the array in O(n).
    '''
    i = 0
    j = len(A) - 1
    pivot = 0
    while i <= j:
        while A[i] == pivot and i < j:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else:
            i += 1
    return A


if __name__ == "__main__":
    A = [0, 1, 1, 0, 0, 0, 1]
    print(one_zero_array(A))
    B = [1, 0, 1, 0, 1, 0]
    print(one_zero_array(B))
    C = [1, 1, 1, 0, 0]
    print(one_zero_array(C))
    D = [0, 0, 0, 0, 1, 1, 0, 1]
    print(one_zero_array(D))
    E = [1, 1, 0, 0, 1, 1, 0, 1]
    print(one_zero_array(E))
