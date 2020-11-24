def left(i):  # Heap
    return i * 2


def right(i):
    return i * 2 + 1


def parent(i):
    return i // 2


def is_max_heap(H):
    n = len(H) - 1
    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
    return True


def max_heapify(H, size, i):
    le = left(i)
    r = right(i)

    if le <= size and H[le] > H[i]:
        largest = le
    else:
        largest = i

    if r <= size and H[r] > H[largest]:
        largest = r

    if largest != i:
        H[i], H[largest] = H[largest], H[i]
        max_heapify(H, size, largest)


def build_max_heap(H):
    size = len(H) - 1
    for i in range(size // 2, 0, -1):
        max_heapify(H, size, i)


def heap_sort(H):  # Heap Sort
    build_max_heap(H)
    size = len(H) - 1
    for i in range(size, 1, -1):
        H[1], H[i] = H[i], H[1]
        size -= 1
        max_heapify(H, size, 1)


def get_maximum(H):  # Priority Queue
    return H[1]


def extract_max(H, size):
    max_item = heap[1]
    heap[1] = heap[size]
    size -= 1
    max_heapify(H, size, 1)
    return max_item


def insert_node_max(H, size, node):
    size += 1
    H[size] = node
    i = size
    while i > 1 and H[i] > H[parent(i)]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)
    return size


# def increase_key(H, i, new_value): pass


if __name__ == '__main__':
    heap = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(f'{heap}\t\t{is_max_heap(heap)}')
    print(heap)
    max_heapify(heap, 9, 3)
    print(heap)
    print('\n\n')
    heap = [None, 19, 7, 17, 3, 5, 12, 10, 1, 4]
    print(f'{heap}\t\t{is_max_heap(heap)}')
    heap = [None, 1, 2, 3]
    print(f'{heap}\t\t{is_max_heap(heap)}')
    max_heapify(heap, 3, 1)
    print(f'{heap}\n\n')
    heap = [None, 2, 1, 3]
    print(f'{heap}\t\t{is_max_heap(heap)}')
    heap = [None, 3, 1, 2]
    print(f'{heap}\t\t{is_max_heap(heap)}')

    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print(f'Before building heap:\n{heap}')
    build_max_heap(heap)
    print(f'After building heap:\n{heap}')

    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print(f'Before sorting:\n{heap}')
    heap_sort(heap)
    print(f'After sorting:\n{heap}')
