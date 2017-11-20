def omega_0(x, p):
    if x >= 0 and x < p - 1:
        return x
    else:
        return 0

def square_omega(x, p):
    assert(x < p)
    return x*(p-x-2) if 0 <= x < p - 1 else 0
