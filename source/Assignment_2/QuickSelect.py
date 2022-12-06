from Partition import partition


def quick_select(A: list, p: int, r: int, d: int):
    if d > 0 and d <= r - p + 1:
        q = partition(A, p, r)
        if q - p == d - 1:
            return A[q]
        if q - p > d - 1:
            return quick_select(A, p, q - 1, d)
        return quick_select(A, q + 1, r, d - q + p - 1)


if __name__ == "__main__":
    A = [5, 30, 1, 9, 15]
    print(quick_select(A, 0, len(A)-1, 1))
    print(quick_select(A, 0, len(A)-1, 2))
    print(quick_select(A, 0, len(A)-1, 3))
    print(quick_select(A, 0, len(A)-1, 4))
    print(quick_select(A, 0, len(A)-1, 5))
