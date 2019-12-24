import random


def heapify_down(A, i, heapsize):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heapsize and A[largest] < A[left]:
        largest = left
    if right < heapsize and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        heapify_down(A, largest, heapsize)


def build_max_heap(A, heapsize):
    for i in range(len(A) // 2, -1, -1):
        heapify_down(A, i, heapsize)



def heapsort(A):
    heapsize = len(A)
    build_max_heap(A, heapsize)
    for i in range(len(A)):
        A[0], A[heapsize-1] = A[heapsize-1], A[0]
        heapsize -= 1
        heapify_down(A, 0, heapsize)


def quicksort(A):
    def _quicksort(A, p, r):
        if p >= r:
            return
        pivot = A[random.randint(p, r)]
        i, j = p, r
        while i <= j:
            while A[i] < pivot: i += 1
            while A[j] > pivot: j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        _quicksort(A, p, j)
        _quicksort(A, i, r)

    _quicksort(A, 0, len(A) - 1)


def mergesort(A):
    def merge(A, p, q, r):
        p1 = 0
        p2 = 0
        left = A[p:q+1]
        right = A[q+1:r+1]
        while p1 < len(left) and p2 < len(right):
            if left[p1] < right[p2]:
                A[p] = left[p1]
                p += 1
                p1 += 1
            else:
                A[p] = right[p2]
                p += 1
                p2 += 1
        while p1 < len(left):
            A[p] = left[p1]
            p += 1
            p1 += 1
        while p2 < len(right):
            A[p] = right[p2]
            p += 1
            p2 += 1

    def _mergesort(A, p, r):
    	if p < r:
            q = (p + r) // 2
            _mergesort(A, p, q)
            _mergesort(A, q + 1, r)
            merge(A, p, q, r)

    _mergesort(A, 0, len(A)-1)

A = [9,9,8,6,34,3,10,2,4,6,4,8,9]
# heapsort(A)
# quicksort(A)
mergesort(A)
print(A)
