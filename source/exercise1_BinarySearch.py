import math
# exercise 1, question 2

def unimodal_index(A: list, n: int):
    '''
    A function which returns an index of a given unimodal array.
    Right to the number of this index,
    all elements are smaller and they are sorted in decreasing order.
    Left to number of this index, 
    all elements are smaller and they are sorted in increasing order.
    '''
    found = False
    min = 0
    max = n-1
    while (found == False and min <= max):
        mid = math.floor((min+max)/2)
        if(A[mid] > A[mid+1] and A[mid] > A[mid-1]):
            found = True
        else:
            if (A[mid] > A[mid+1]):
                max = mid - 1
            else:
                min = mid + 1
    if found == True:
        return mid


if __name__ == "__main__":
    print(unimodal_index(A=[1,3,7,10,8,5,3], n=7))
    print(unimodal_index(A=[1,10,9,8,7,6,5], n=7))
    print(unimodal_index(A=[1,2,9,8,7,6,5], n=7))



