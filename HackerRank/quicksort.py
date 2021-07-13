

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[i], A[hi] = A[hi], A[i]

    return i



arr = [7, 2, 1, 8, 6, 3, 5, 4]

l = 0
h = len(arr)-1


quicksort(arr, l, h)
print(arr)

