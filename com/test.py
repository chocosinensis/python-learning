print('\u001b[36mHello, World!', '\u001b[39m\n')

a = input('Enter a: ')
b = input('Enter b: ')
add = int(a) + int(b)
print('The sum is: ', add, '\n')

add = 0
i = 1
while i <= 9:
    add += i
    i = i + 1
print('The sum is: ', add, '\n')

hello = 'Hello, World!\n' \
        'I am Saqib. How are you?\n' \
        'In Sha Allah -\t If Allah wills.\n' \
        'Ma Sha Allah -\t Whatever Allah wills.'
print(hello, '\n')

sec = 3600
s = int(sec % 60)
minute = sec / 60
m = int(minute % 60)
h = minute / 60
print(sec, 's = ', h, 'h', m, 'm', s, 's', '\n')


def double(num):
    """Function to double the value"""
    return 2 * num


print(double.__doc__, '\n')

for fg in range(30, 37):
    for bg in range(40, 47):
        print(chr(27) + '[%d;%dm~TEST~' % (fg, bg), end='')
    print(chr(27) + '[0m')
print('\n')
print(chr(27) + '[34;47;1;3m CRAZY TEXT', chr(27) + '[0m')
print('\n')
for i in range(1, 9):
    print(chr(27) + '[%dm~TEST~ ' % i, chr(27) + '[0m', end='')
print('\n')

Python = chr(27) + "[34m ____\t\t\t _     _\n" \
                   "|  _  \\ \t\t| |__ | |\n" \
                   "| |_|  | _   _	|  __|| |___   ___   _  ___\n" \
                   "| ___ /\t| | | | | |   |  _  \\ / _ \\ | |' _ \\\n" \
                   "| |\t\t| |_| | | |__ | | | || |_| || |,' | |\n" \
                   "|_|\t\t\\___  | \\____||_| |_| \\___/ |__|  |_|\n" \
                   "\t\t ___| |\n" \
                   "\t\t(_____/" + chr(27) + "[39m"
print(Python)

a = 5
print(a, 'is of type', type(a))
a = 2.0
print(a, 'is of type', type(a))
a = 1 + 2j
print(f'\nIs {a} complex number?', isinstance(1 + 2j, complex), '\n')

a, b, c = 5, 3.2, 'Hello'
print(a, '\n', b, '\n', c)
x = y = z = 'same'
print(x, '\n', y, '\n', z, '\n')

a, b, c, d = 0b1010, 100, 0o310, 0x12c
float_1, float_2 = 10.5, 1.5e2
x = 1 + 2j
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real, '\n')

fruits = ['Apple', 'Mango', 'Orange']
numbers = (1, 2, 3)
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
vowels = {'a', 'e', 'i', 'o', 'u'}
print(fruits, '\n', numbers, '\n', alphabets, '\n', vowels, '\n')

a = [5, 10, 15, 20, 25, 30, 35, 40]
print('a[2] =', a[2])
print('a[0:3] =', a[0:3])
print('a[5:] =', a[5:])
a = {5, 2, 1, 3, 4}
print('a =', a)
a = {1, 1, 2, 2, 3, 3, 3}
print('a =', a)

d = {1: 'value', 'key': 2}
print(type(d))
print(d, '\n', d[1], '\n', d['key'], '\n')

num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print(f'data type of num_int:{type(num_int)}\ndata type of num_flo:{type(num_flo)}')
print(f'value of num_new:{num_new}\ndata type of num_new:{type(num_new)}\n')
