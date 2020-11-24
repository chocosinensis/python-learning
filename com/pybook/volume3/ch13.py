def merge(a, b):
    merged = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged.append(a[index_a])
            index_a += 1
        else:
            merged.append(b[index_b])
            index_b += 1

    if index_a < len_a:
        merged.extend(a[index_a:])
    elif index_b < len_b:
        merged.extend(b[index_b:])

    return merged


def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    return merge(left, right)


def partition(L, low, high):
    pivot = L[high]
    i = low - 1
    for j in range(low, high):
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    return i + 1


def quick_sort(L, low, high):
    if low >= high:
        return
    p = partition(L, low, high)
    quick_sort(L, low, p - 1)
    quick_sort(L, p + 1, high)


def counting_sort(L):
    count = [0] * 11
    for x in L:
        count[x] += 1
    sort = []
    for index, value in enumerate(count):
        if value > 0:
            sort.extend([index] * value)
    return sort


if __name__ == '__main__':
    scenarios = [
        {'a': [1], 'b': [2], 'expected': [1, 2]},
        {'a': [2], 'b': [1], 'expected': [1, 2]},
        {'a': [], 'b': [1, 2], 'expected': [1, 2]},
        {'a': [1, 2], 'b': [], 'expected': [1, 2]},
        {'a': [1, 3, 5, 6], 'b': [2, 4, 7, 8], 'expected': [1, 2, 3, 4, 5, 6, 7, 8]},
        {'a': [1], 'b': [2, 3, 4], 'expected': [1, 2, 3, 4]},
    ]
    for item in scenarios:
        merged_li = merge(item['a'], item['b'])
        assert item['expected'] == merged_li

    li = [[4, 7, 2, 3], [10], [10, 9, 8, 7, 6], [2, 3, 1], [1, 2], [2, 1]]
    for a_li in li:
        sorted_li = merge_sort(a_li)
        print(f'Original list: {a_li}\nSorted list: {sorted_li}\n')

    li = [1, 5, 6, 3, 8, 4, 7, 2]
    print(f'Before sort: {li}')
    quick_sort(li, 0, len(li) - 1)
    print(f'After sort: {li}')

    li = [3, 4, 1, 6, 2, 4, 9, 7, 8, 4, 2, 1]
    print(f'Before sort: {li}')
    print(f'After sort: {counting_sort(li)}')
