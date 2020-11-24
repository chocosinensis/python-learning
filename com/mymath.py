import math

pi = math.pi
e = math.e


def pow(a, b):
    return a ** b


def abs(n):
    return n if n > 0 else -n


def sqrt(n):
    return pow(n, 1.0 / 2.0)


def min(a, b):
    return a if a < b else b


def max(a, b):
    return a if a > b else b


def exp(n):
    return pow(e, n)


def pow_10(n):
    return pow(10, n)


def ln(n):
    return math.log(n, e)


def log(n):
    return log_a(n, 10.0)


def log_a(n, a):
    return ln(n) / ln(a)


def ang_to_rad(deg):
    return deg * pi / 180.0


def ang_to_deg(rad):
    return rad * 180.0 / pi


def sin(angle):
    return math.sin(ang_to_rad(angle))


def cos(angle):
    return math.cos(ang_to_rad(angle))


def tan(angle):
    return math.tan(ang_to_rad(angle))


def factorial(n):
    return 1 if n in [0, 1] else n * factorial(n - 1)
