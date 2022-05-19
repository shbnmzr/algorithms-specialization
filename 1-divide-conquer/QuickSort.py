import random


def quick_sort(A: list):
    n = len(A)
    if n <= 1:
        return list(A)
    else:
        pivot = A[choose_pivot_randomly(n)]
        partitioned = partition(A, pivot)
        pivot_index = A.index(pivot)

        A[:pivot_index] = quick_sort(partitioned[ :pivot_index])
        
        A[pivot_index+1:] = quick_sort(partitioned[pivot_index+1: ])
        return A


def partition(A: list, pivot: int) -> list:
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


def choose_pivot_randomly(n: int):
    pivot_index = random.randint(0, n-1)
    return pivot_index


def swap(A: list, first_index: int, second_index: int):
    A[first_index], A[second_index] = A[second_index], A[first_index]
    return A


def main():
    with open('./QuickSortTest.txt', 'r') as file:
        lines = file.read().splitlines()
        numbers = [int(x) for x in lines]

    res = quick_sort(numbers)
    print(res)


if __name__=='__main__':
    main()