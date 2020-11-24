def fib(n):  # Ch 2
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def list_fib(li):
    return [fib(n) for n in range(li + 1)]


if __name__ == '__main__':
    for i in range(11):
        print(fib(i), end=' ')
    print()
    print(list_fib(1))
    print(list_fib(2))
    print(list_fib(10))
