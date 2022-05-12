def merge_sort(A):
    n = len(A)
    if n <= 2:
        if n == 2:
            if A[0] > A[1]:
                return [A[1], A[0]]
        return A.copy()
    else:
        left = merge_sort(A[:n // 2])
        right = merge_sort(A[n // 2:])
        merged = merge_sorted_lists(left, right)
        return merged

def merge_sorted_lists(l1, l2):
    i = 0
    j = 0
    merged = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    if i < len(l1):
        merged.extend(l1[i:])
    if j < len(l2):
        merged.extend(l2[j:])
    return merged


def main():
    with open('test.txt', 'r') as file:
        lines = file.read().splitlines()
        numbers = [int(x) for x in lines]
    print(merge_sort(numbers))
    


if __name__ == '__main__':
    main()
