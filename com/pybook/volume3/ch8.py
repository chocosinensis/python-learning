def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def binary_search(L, left, right, x):
    if left > right:
        return -1
    mid = (left + right) // 2
    if L[mid] == x:
        return mid
    elif L[mid] > x:
        return binary_search(L, left, mid - 1, x)
    else:
        return binary_search(L, mid + 1, right, x)


if __name__ == '__main__':
    for i, fact in enumerate([1, 1, 2, 6, 24, 120, 720]):
        print(f'{i}! = {factorial(i)}')
        assert factorial(i) == fact
    print('\nn:\tfib(n):')
    for i, fibo in enumerate([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
        print(f'{i}\t{fib(i)}')
        assert fib(i) == fibo
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'\n\n\nList: {li}\n\nTesting Algorithm:\n\t binary_search() :\n')
    le, ri = 0, len(li) - 1
    for item in range(11):
        position = binary_search(li, le, ri, item)
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
