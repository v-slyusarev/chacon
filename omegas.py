def omega_0(x, p):
    if x >= 0 and x < p - 1:
        return x
    else:
        return 0


def square_omega_1(x, p):
    assert x < p
    return x * (p - x - 1) if 0 <= x < p - 1 else 0


def square_omega_2(x, p):
    assert x < p
    return x * (p - x) if 0 <= x < p - 1 else 0