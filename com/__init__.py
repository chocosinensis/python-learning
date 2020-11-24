
def console():
    command = input('>>> ')
    while command != 'quit':
        try:
            eval(command)
        except NameError:
            print(f'\'{command}\'')
        except Exception as e:
            print(e)
        command = input('>>> ')


def myfun():
    return True if None is True and None is not False else False if None is not True or None is False else None is None and None is not None


def mydec(func):
    def dec(*args, **kwargs):
        print(args)
        func()
        print(kwargs)
    return dec


@mydec
def lol():
    print('lol')


if __name__ == '__main__':
    console()
