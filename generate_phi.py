from copy import deepcopy
from intersect import intersect
_P_ = 3

def omega_0(x):
    if (x >= 0 and x < _P_ - 1):
        return x
    else:
        return 0

omega = omega_0


def z_p_func_template():
    return {'blocks': []}


def phi_by_omega():
    phi = z_p_func_template()

    for i in range(_P_-1):
        phi['blocks'] += [(['z', i+1], omega(i))]

    return phi


def plus_one(y0):
    Y = [y0]

    k = 0
    t = 1
    explode = False
    for digit in y0:
        if digit == 'z' and t > 0:
            explode = True
            break
        t = 0 if (digit + t < _P_) else 1
        if t == 0:
            break
        k += 1

    if explode:
        y1 = deepcopy(y0)
        y1.remove('z')
        y2 = deepcopy(y0)
        y2.insert(k, 0)
        Y = [y1, y2]

    Z = []
    for y in Y:
        z = []
        t = 1
        for digit in y:
            if t > 0:
                digit2 = (digit + t) % _P_
                t = 0 if (digit + t < _P_) else 1
                z.append(digit2)
            else:
                z.append(digit)
        Z.append(z)

    return Z


def plus_one_to_block(block):
    a = plus_one(block[0])
    b = []
    for s in a:
        b.append((s, block[1]))
    return b


def shift(f):
    f2 = deepcopy(f)
    f2['blocks'] = []
    for block in f['blocks']:
        b = plus_one_to_block(block)
        f2['blocks'] += b
    return f2


def add(f1, f2):
    f = deepcopy(f1)
    f['blocks'] = []
    for block1 in f1['blocks']:
        for block2 in f2['blocks']:
            a = intersect(block1[0], block2[0])
            for s in a:
                f['blocks'].append((s, block1[1] + block2[1]))
    return f


def generate_phi_m(PHI, m_max, p=3):
    _P_ = p

    for m in range(1, m_max + 1):
        if m in PHI:
            continue
        if (m == 1):
            PHI[1] = phi_by_omega()
        if(m != 1):
            PHI[m] = add(PHI[m-1], shift(PHI[m-1]))





