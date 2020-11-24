import io  # Ch 5

filename = r'D:\$@q!b\Files\Java\python_test.txt'
mode = 'r'

try:
    with open(filename, mode) as fr:
        content = fr.read()
        print(content)
except FileNotFoundError:
    print(f'\u001b[31m{filename} is not correct. Please check if the name is correct.\u001b[39m')
except io.UnsupportedOperation:
    print(f'\u001b[31mAre you sure {filename} is readable?\u001b[39m')

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('\u001b[31mCan\'t divide by zero\u001b[39m')
    except TypeError:
        print('\u001b[31mUnsupported type. Did you use String?\u001b[39m')


if __name__ == '__main__':
    print(div(10, 2))
    print(div(3, 0))
    print(div(9, 3))
    print(div('12', 3))

class Vehicle:  # Ch 6
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print(f'Driving {self.manufacturer} {self.name}')

    def turn(self, direction):
        print(f'Turning {self.name} to {direction}')

    def brake(self):
        print(f'Applying brakes to {self.name}')


class Car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 4

    def turn(self, direction):
        print(f'{self.name} is turning {direction}')
