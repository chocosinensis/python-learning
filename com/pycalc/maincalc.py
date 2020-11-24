from . import process, InvalidStatementError
from .commands import *

if __name__ == '__main__':
    handlers = [
        Adder(), Subtractor(), Multiplier(), Divider(), PowerTo()
    ]

    print('Please type your command')
    command = input()

    while command != 'quit':
        try:
            print(process(handlers, command))
        except InvalidStatementError as e:
            print(f'\u001b[31m{e}\u001b[39m')
        command = input()
