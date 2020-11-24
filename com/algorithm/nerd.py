
def greedy():
    solution_set = list()
    coins = [5, 2, 1]
    sum = 0
    while sum != 28:
        for i in range(len(coins)):
            c = coins[i]
            if sum + c > 28:
                continue
            else:
                sum += c
                solution_set.append(c)
                break
    print(f'{sum}\n{coins}\n{solution_set}')


if __name__ == '__main__':
    graph = {
        '0': {'1', '2'},
        '1': {'0', '3', '4'},
        '2': {'0'},
        '3': {'1'},
        '4': {'2', '3'}
    }
