from sympy import symbols
x = symbols('x')
from fractions import Fraction


def prob(s, p):
    pr = 1
    for digit in s:
        pr *= (Fraction(p, p - 1) if digit == 'z' else Fraction(1, p))
    return pr


def integrate(f, p):
    integral = 0
    for block in f['blocks']:
        integral += prob(block[0], p) * (x**block[1])
    return integral