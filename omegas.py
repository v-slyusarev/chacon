import legendre

def omega_0(x, p):
    if x >= 0 and x < p - 1:
        return x
    else:
        return 0
# all symmetric


def square_omega_1(x, p):
    assert x < p
    return x * (p - x - 1) if 0 <= x < p - 1 else 0
# symmetric only for p=3


def square_omega_2(x, p):
    assert x < p
    return x * (p - x) if 0 <= x < p - 1 else 0
# symmetric only for p=3


def square_omega_3(x, p):
    assert x < p
    return x**2 if 0 <= x < p - 1 else 0
# symmetric only for p=3


def linear_omega_1(x, p):
    return 41 * omega_0(x, p)
# all symmetric


def linear_omega_2(x, p):
    return omega_0(x, p) + 41
# all symmetric


def step_omega(x, p):
    if p % 2 == 1:
        return 0 if x < (p - 1) / 2 else 1
    if p % 2 == 0:
        if x < p / 2 - 1:
            return 0
        else:
            if x == p / 2 - 1:
                return 1
            else:
                return 2
# all symmetric


def legendre_omega(x, p):
    return legendre.calculateLegendre(x + 1, p) + 1
# symmetric unless p is pythagorean prime
# for pythagorean primes symmetric unless m=3