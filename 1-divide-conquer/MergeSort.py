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
    if i + j == len(l1) + len(l2) - 2:
        return merged
    if i < len(l1):
        merged.extend(l1[i:])
        return merged
    if j < len(l2):
        merged.extend(l2[j:])
        return merged


def main():
    print(merge_sorted_lists([1, 3, 5, 7], [1, 2, 4, 6]))
    print(merge_sorted_lists([1, 3, 5, 7], [1, 2, 4, 6, 8]))
    print(merge_sorted_lists([1, 3, 5, 7], [9, 11, 13, 14, 15, 16]))


if __name__ == '__main__':
    main()
