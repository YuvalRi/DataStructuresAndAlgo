from Merge import merge

def merge_sort(A: list, p: int, r: int):
    if p > r:
        return f'Please make sure that r index is bigger than p index!'
    elif p < r:
        q = p+(r-p)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A


if __name__ == "__main__":
    A = [40, 20, 10, 80, 60, 50, 7, 30, 100]
    print(merge_sort(A, 0, len(A)-1))
    B = [40, 20, 10]
    print(merge_sort(B, 0, len(B)-1))
    C = [8]
    print(merge_sort(C, 0, len(C)-1))
    D = [8,9,2,5]
    print(merge_sort(D, 5, 3))

