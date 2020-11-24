# Searching Algorithms
def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i

    return -1


def binary_search(L, x):
    left, right = 0, len(L) - 1

    while left <= right:
        mid = (left + right) // 2

        if L[mid] == x:
            return mid

        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Sorting Algorithms
def selection_sort(L):
    """
    8, 2, 4, 1, 5, 7    Selection sort example  \n
    1, 2, 4, 8, 5, 7                            \n
    1, 2, 4, 5, 8, 7                            \n
    1, 2, 4, 5, 7, 8
    """
    n = len(L)

    for i in range(n - 1):
        index_min = i

        for j in range(i + 1, n):
            if L[j] < L[index_min]:
                index_min = j

        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]


def bubble_sort(L):
    """
    3, 1, 7, 6, 2       Bubble sort example     \n
    1, 3, 7, 6, 2                               \n
    1, 3, 6, 7, 2                               \n
    1, 3, 6, 2, 7                               \n
    1, 3, 2, 6, 7                               \n
    1, 2, 3, 6, 7
    """
    n = len(L)

    for i in range(n):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


def insertion_sort(L):
    """
    5, 4, 3, 2, 1       Insertion sort example  \n
    4, 5, 3, 2, 1                               \n
    3, 4, 5, 2, 1                               \n
    2, 3, 4, 5, 1                               \n
    1, 2, 3, 4, 5
    """
    n = len(L)

    for i in range(1, n):
        item = L[i]
        j = i - 1

        while j >= 0 and L[j] > item:
            L[j + 1] = L[j]
            j -= 1

        L[j + 1] = item


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
    count = [0] * 10
    for x in L:
        count[x] += 1
    sort = []
    for index, value in enumerate(count):
        if value > 0:
            sort.extend([index] * value)

    for i in range(len(L)):
        L[i] = sort[i]


def digits(num):
    temp = num
    count = 0
    while temp > 0:
        temp //= 10
        count += 1
    return count


def counting_radix(L, place):
    size = len(L)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = L[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = L[i] // place
        output[count[index % 10] - 1] = L[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        L[i] = output[i]


def radix_sort(L):
    max_element = max(L)
    x = digits(max_element)
    place = 1
    for i in range(x):
        counting_radix(L, place)
        place *= 10


def bucket_sort(L):
    buckets = []
    for i in range(len(L)):
        buckets.append([])

    for i in L:
        i_b = i // 10
        buckets[i_b].append(i)
    for i in range(len(L)):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(len(L)):
        for j in range(len(buckets[i])):
            L[k] = buckets[i][j]
            k += 1


def shell_sort(L):
    interval = len(L) // 2
    while interval > 0:
        for i in range(interval, len(L)):
            item = L[i]
            j = i

            while j >= interval and L[j - interval] > item:
                L[j] = L[j - interval]
                j -= interval

            L[j] = item

        interval //= 2
