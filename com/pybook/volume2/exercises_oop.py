from .main_oop import Vehicle  # import for Ch 6

class Car:  # Ch 3
    def __init__(self, name, manufacturer, color, year, cc):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc

    def __str__(self):
        return 'Details of the car:\n' \
               f'Name: {self.name}\nManufacturer: {self.manufacturer}\n' \
               f'Color: {self.color}\nYear created: {self.year}\nCapacity of Engine (cc): {self.cc}'

    def start(self):
        print(f'Starting the engine of {self.name}')

    def brake(self):
        print(f'Brakes of {self.name} activated')

    def drive(self):
        print(f'Driving {self.name}')

    def turn(self, turning):
        print(f'Turning {self.name} in direction: {turning}')

    def change_gear(self, gear):
        print(f'Changing gear of {self.name} to: {gear}')


class MotorCycle(Vehicle):  # Ch 6
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 2

    def drive(self):
        print(f'Starting {self.manufacturer} {self.name}')


class TurtleError(Exception):  # Exception for Ch 6
    def __init__(self, cause='Turning AjobTurtle to right',
                 message='I don\'t turn right cause I am Ajob!'):
        self.cause = cause
        self.message = message

    def __str__(self):
        return f'{self.cause}: {self.message}'
