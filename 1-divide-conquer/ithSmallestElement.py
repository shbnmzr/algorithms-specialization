import random


def RSelect(A: list, i: int):
    n = len(A)
    if n == 1:
        return A[0]
    else:
        pivot = choose_pivot_randomly(A)
        partitioned = partition(A, pivot)
        pivot_index = partitioned.index(pivot)

        if i == pivot_index+1:
            return pivot
        if i > pivot_index+1:
            return RSelect(A[pivot_index+1:], i-pivot_index-1)
        else:
            return RSelect(A[:pivot_index], i)


def partition(A: list, pivot: int):
    n = len(A)
    i = 1
    A = swap(A, A.index(pivot), 0)
    for j in range(1, n):
        if j == A.index(pivot):
            continue
        if A[j] < pivot:
            A = swap(A, i, j)
            i += 1
            j += 1

    i -= 1
    A = swap(A, i, 0)
    return A


def swap(A: list, first_index: int, second_index: int):
    A[first_index], A[second_index] = A[second_index], A[first_index]
    return A


def choose_pivot_randomly(A: list):
    pivot = random.randrange(0, len(A)-1)
    return A[pivot]


def main():
    print(RSelect([3,5,6,2,0,121,45,-1,-121212,87283], 5))


if __name__=='__main__':
    main()