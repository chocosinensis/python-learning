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

    for i in range(0, n):
        for j in range(0, n - i - 1):
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


if __name__ == '__main__':
    li = [8, 2, 4, 1, 5, 7]
    print(f'Before sort: {li}')
    selection_sort(li)
    print(f'After sort: {li}')
    li = [3, 1, 7, 6, 2]
    print(f'Before sort: {li}')
    bubble_sort(li)
    print(f'After sort: {li}')
    li = [5, 4, 3, 2, 1]
    print(f'Before sort: {li}')
    insertion_sort(li)
    print(f'After sort: {li}')
