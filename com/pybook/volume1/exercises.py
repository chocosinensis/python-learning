# Ch 2
number1 = int(input('Enter an integer: '))
number2 = int(input('Enter another integer: '))

add = number1 + number2
sub = number1 - number2
mul = number1 * number2
div = number1 / number2
mod = number1 % number2
int_div = number1 // number2
exp = number1 ** number2

print(f'{number1} + {number2} = {add}\n{number1} - {number2} = {sub}\n'
      f'{number1} * {number2} = {mul}\n{number1} / {number2} = {div}\n'
      f'{number1} % {number2} = {mod}\n{number1} // {number2} = {int_div}\n'
      f'{number1} ** {number2} = {exp}')


# Ch 3
num = float(input('Enter a number: '))
if num > 0:
    print(f'Your entered number {num} is positive')
elif num < 0:
    print(f'Your entered number {num} is negative')
else:
    print('Your entered number is %.0f' % num)

num = float(input('Enter a number: '))
if num % 2 == 0:
    print('The number is an even number')
else:
    print('The number is an odd number')

year = int(input('Enter a year: '))
if year % 4 != 0:
    print(f'The year {year} is not leap')
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The year {year} is leap')
        else:
            print(f'The year {year} is not leap')
    else:
        print(f'The year {year} is leap')

if year % 400 == 0:
    print(f'The year {year} is leap')
elif year % 100 == 0:
    print(f'The year {year} is not leap')
elif year % 4 == 0:
    print(f'The year {year} is leap')
else:
    print(f'The year {year} is not leap')

if year % 100 != 0 and year % 4 == 0:
    print(f'The year {year} is leap')
elif year % 100 == 0 and year % 400 == 0:
    print(f'The year {year} is leap')
else:
    print(f'The year {year} is not leap')


# Ch 6
def average_list(a_list):
    sum = 0
    for item in a_list:
        sum += item
    return sum / len(a_list)


def time_table(n=1):
    for i in range(11):
        print(f'{n} * {i} = {n * i}')


# Ch 7
str1 = input('Enter a string: ')
str_reversed = ''.join(reversed(str1))
if str1.lower() == str_reversed.lower():
    print('The word is a palindrome')
else:
    print('The word is not a palindrome')

str2 = input('Enter a string: ')
a = b = c = d = ''
for letter in range(len(str2)):
    if str2[letter] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        a += str2[letter]
    elif str2[letter] in 'abcdefghijklmnopqrstuvwxyz':
        b += str2[letter]
    elif str2[letter] in '0123456789':
        c += str2[letter]
    else:
        d += str2[letter]
print(f'{a}\n{b}\n{c}\n{d}')

str3 = input('Enter a string: ')
str_li = [ch for ch in str3]
for i in range(0, len(str_li) - 1, 2):
    str_li[i], str_li[i + 1] = str_li[i + 1], str_li[i]
print(f'\n{str3}\n{"".join(str_li)}\n')


# Ch 8.1
def square_list(L):
    return [x * x for x in L]


# Ch 8.2
Bangladesh = {
    'Dhaka': {'District': 13, 'Upazila': 93, 'Union': 1833},
    'Chattogram': {'District': 11, 'Upazila': 97, 'Union': 336},
    'Khulna': {'District': 10, 'Upazila': 59, 'Union': 270},
    'Rajshahi': {'District': 8, 'Upazila': 70, 'Union': 558},
    'Barishal': {'District': 6, 'Upazila': 39, 'Union': 333},
    'Rangpur': {'District': 8, 'Upazila': 58, 'Union': 536},
    'Sylhet': {'District': 4, 'Upazila': 38, 'Union': 334},
    'Mymensingh': {'District': 4, 'Upazila': 34, 'Union': 350}
}

def add_dict(dict=None, dict2=''):
    if dict is None:
        dict = Bangladesh
    sum = 0
    for item in dict.keys():
        sum += dict[item][dict2]
    return sum


print('Total districts in Bangladesh:', add_dict(dict2='District'))
print('Total upazilas in Bangladesh:', add_dict(dict2='Upazila'))
print('Total unions in Bangladesh:', add_dict(dict2='Union'))
