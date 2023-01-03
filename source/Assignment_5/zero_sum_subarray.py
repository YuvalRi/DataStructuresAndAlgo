# The solution below based on Vikas Chitturi solution
# in geeksforgeeks site.

def zero_sum_subarray(A, n):
    '''
    Input: A - an array of integers, n - length of A
    Output: List of tuples, where each tuple represents
    the start and end indices of a subarray 'A' that has
    a sum of zero
    '''
    # creating an empty dictionary
    hash_table = {}
    # creating an empty list
    out = []
    # tracker for sum of elements
    sum = 0
    for i in range(n):
        # increment sum by element of array
        sum += A[i]
        # if sum is 0, we found a subarray starting
        # from index 0 and ending at index i
        if sum == 0:
            out.append((0, i))
        al = []
        # if sum already exists in the map
        # there exists at least one subarray
        # ending at index i with 0 sum
        if sum in hash_table:
            # map[sum] stores starting index of
            # all subarrays
            al = hash_table.get(sum)
            for j in range(len(al)):
                out.append((al[j]+1, i))
        al.append(i)
        hash_table[sum] = al
    return out


def print_message(output):
    '''
    A function that prints all subarrays
    with sum zero if exist. Otherwise, it
    will print 'No subarray exists'
    '''
    if (len(output) == 0):
        print("No subarray exists")
    for i in output:
        print("Subarray found from index " + str(i[0]) + " to " + str(i[1]))


if __name__ == "__main__":
    arr_1 = [0, -2, 2, 5, 6, 3]
    n = len(arr_1)
    out = zero_sum_subarray(arr_1, n)
    print(out)
    print_message(out)
    arr_2 = [3, -1, 1, -3, 6, 4]
    n = len(arr_2)
    out = zero_sum_subarray(arr_2, n)
    print_message(out)
    arr_3 = [1, 2, 3, 4, 5, 6]
    n = len(arr_3)
    out = zero_sum_subarray(arr_3, n)
    print_message(out)
