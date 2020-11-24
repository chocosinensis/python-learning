
class MathProcessable:
    separator = ' '

    def keyword(self): pass

    def symbol(self): pass

    def do_calc(self, left_val, right_val): pass


class CalculateBase:
    def __init__(self):
        self.left_val = 0
        self.right_val = 0
        self.result = 0

    def calculate(self): pass


def process(handlers, statement):
    parts = statement.split(MathProcessable.separator)
    if len(parts) != 3:
        raise InvalidStatementError("Incorrect number of fields", statement)

    keyword = parts[0]
    the_handler = None
    for handler in handlers:
        if keyword == handler.keyword():
            the_handler = handler
            break

    if the_handler is None:
        raise InvalidStatementError("Command not found", statement)

    try:
        left_val = float(parts[1])
        right_val = float(parts[2])
        result = the_handler.do_calc(left_val, right_val)
    except Exception as e:
        raise InvalidStatementError("Exception caused", e)

    return f'{left_val} {the_handler.symbol()} {right_val} = {result}'


class InvalidStatementError(Exception):
    def __init__(self, reason, statement):
        super(InvalidStatementError, self).__init__(f'{reason}: {statement}')
