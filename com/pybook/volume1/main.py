print('\u001b[34mHello, World!\u001b[39m')  # Ch 1

name = input('What is your name?\n')  # Ch 2
print(f'Welcome to Python, \u001b[34m{name}\u001b[39m!')

marks = int(input('Enter your marks: '))  # Ch 3
if marks >= 80:
    grade = '\u001b[34mA+\u001b[39m'
elif marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'A-'
elif marks >= 50:
    grade = 'B'
else:
    grade = '\u001b[31mF\u001b[39m'

print('Your grade is: ' + grade)

terminate = False  # Ch 5
while not terminate:
    number1 = int(input('Please enter a number: '))
    number2 = int(input('Please enter another number: '))

    while True:
        operation = input('Please enter \'add\', \'sub\' or \'quit\' to exit: ')
        if operation == 'quit':
            terminate = True
            break
        if operation not in ['add', 'sub']:
            print('Unknown operation')
            continue
        if operation == 'add':
            print(f"{number1} + {number2} = {number1 + number2}")
            break
        if operation == 'sub':
            print(f"{number1} - {number2} = {number1 - number2}")
            break
