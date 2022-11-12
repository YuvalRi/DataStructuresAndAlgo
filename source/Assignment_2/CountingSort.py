# CountingSort algorithm

def counting_sort(A: list, n: int, k: int):
    output = [0] * n
    new_arr = [0] * k

    for j in range(0, n):
        new_arr[A[j]] += 1

    for j in range(1, k):
        new_arr[j] += new_arr[j - 1]

    j = n - 1
    while j >= 0:
        output[new_arr[A[j]]-1] = A[j]
        new_arr[A[j]] -= 1
        j -= 1

    for j in range(0, n):
        A[j] = output[j]

if __name__ == "__main__":
    data = [3,5,1,6,7,8,3]
    counting_sort(data, len(data), 9)
    print("Sorted Array: ")
    print(data)
    data_2 = [5, 3, 5, 2, 12, 1, 7, 3, 8 ,2]
    counting_sort(data_2, len(data_2), 13)
    print("Sorted Array: ")
    print(data_2)


