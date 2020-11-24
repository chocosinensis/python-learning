from . import MathProcessable, CalculateBase

class Adder(MathProcessable, CalculateBase):
    def calculate(self):
        self.result = self.left_val + self.right_val

    def keyword(self): return 'add'

    def symbol(self): return '+'

    def do_calc(self, left_val, right_val):
        self.left_val = left_val
        self.right_val = right_val
        self.calculate()

        return self.result


class Subtractor(MathProcessable, CalculateBase):
    def calculate(self):
        self.result = self.left_val - self.right_val

    def keyword(self): return 'subtract'

    def symbol(self): return '-'

    def do_calc(self, left_val, right_val):
        self.left_val = left_val
        self.right_val = right_val
        self.calculate()

        return self.result


class Multiplier(MathProcessable, CalculateBase):
    def calculate(self):
        self.result = self.left_val * self.right_val

    def keyword(self): return 'multiply'

    def symbol(self): return '*'

    def do_calc(self, left_val, right_val):
        self.left_val = left_val
        self.right_val = right_val
        self.calculate()

        return self.result


class Divider(MathProcessable, CalculateBase):
    def calculate(self):
        self.result = self.left_val / self.right_val

    def keyword(self): return 'divide'

    def symbol(self): return '/'

    def do_calc(self, left_val, right_val):
        if right_val == 0:
            raise UnableToCalcError("You cannot divide by 0 (Zero)")

        self.left_val = left_val
        self.right_val = right_val
        self.calculate()

        return self.result


class PowerTo(MathProcessable, CalculateBase):
    def calculate(self):
        self.result = self.left_val ** self.right_val

    def keyword(self): return 'power'

    def symbol(self): return '^'

    def do_calc(self, left_val, right_val):
        self.left_val = left_val
        self.right_val = right_val
        self.calculate()

        return self.result


class UnableToCalcError(Exception):
    def __init__(self, reason):
        super(UnableToCalcError, self).__init__(reason)
