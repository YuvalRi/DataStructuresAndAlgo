def binary_search(n: int, A: list, x: int):
    start = 0
    end = n-1
    found = False
    while found == False and start <= end:
        mid = (start+end)//2
        if A[mid] == x:
            found = True
        elif x < A[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if found == True:
        return mid
    else:
        return -1 


if __name__ == "__main__":
    lst1 = [1,2,3,4,5,6]
    print(binary_search(n = len(lst1), A = lst1, x = 1))
    print(binary_search(n = len(lst1), A = lst1, x = 2))
    print(binary_search(n = len(lst1), A = lst1, x = 3))
    print(binary_search(n = len(lst1), A = lst1, x = 4))
    print(binary_search(n = len(lst1), A = lst1, x = 5))
    print(binary_search(n = len(lst1), A = lst1, x = 7))



