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


if __name__ == '__main__':
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'List: {li}\n\n')
    print('Testing Algorithm:\n\t linear_search() :\n')
    for item in range(11):
        position = linear_search(li, item)
        if position == -1:
            if item in li:
                print(f'{item} is in {li}, but function returned: -1')
            else:
                print(f'{item} is not in {li}')
        else:
            if li[position] == item:
                print(f'{item} found in correct position: {position}')
            else:
                print(f'linear_search() returned {position} for {item}, which is incorrect')
    print('\n\n\nTesting Algorithm:\n\t binary_search() :\n')
    for item in range(11):
        position = binary_search(li, item)
        if position == -1:
            if item in li:
                print(f'{item} is in {li}, but function returned: -1')
            else:
                print(f'{item} is not in {li}')
        else:
            if li[position] == item:
                print(f'{item} found in correct position: {position}')
            else:
                print(f'binary_search() returned {position} for {item}, which is incorrect')
