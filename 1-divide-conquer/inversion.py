def inversion(A: list):
    n = len(A)
    if n <= 2:
        if n == 2:
            if A[0] > A[-1]:
                return 1, list([A[-1], A[0]])
        return 0, A.copy()

    else:
        inversion_counter = 0

        left = inversion(A[: n//2])
        inversion_counter += left[0]
        left = list(left[1])

        right = inversion(A[n//2: ])
        inversion_counter += right[0]
        right = list(right[1])

        split = split_inversion(left, right)
        inversion_counter += split[0]
        A = split[1]

    return inversion_counter, A

def split_inversion(left: list, right: list):
    split_inversion_counter = 0
    combined = list()
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
            split_inversion_counter += len(left[i:])
        
    if i < len(left):
        combined.extend(left[i:])
    if j < len(right):
        combined.extend(right[j:])

    return split_inversion_counter, combined.copy()



def main():
    with open('./test.txt', 'r') as file:
        lines = file.read().splitlines()
        numbers = [int(x) for x in lines]

    res = inversion(numbers)
    print('Number of inversions: ' + res[0])

if __name__=='__main__':
    main()