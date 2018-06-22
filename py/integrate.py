from sympy import symbols
x = symbols('x')
from fractions import Fraction


def prob(s, p):
    pr = 1
    for digit in s:
        pr *= (Fraction(p, p - 1) if digit == 'z' else Fraction(1, p))
    return pr


def integrate(f, p, mode='polynomial'):
    if mode=='polynomial':
        integral = 0
        for block in f:
            integral += prob(block[0], p) * (x**block[1])
    if mode=='list':
        max_deg = max([block[1] for block in f])
        integral = [0 for i in range(max_deg + 1)]
        for block in f:
            integral[block[1]] += prob(block[0], p)
    return integral