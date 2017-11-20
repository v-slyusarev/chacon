from copy import deepcopy
from intersect import intersect


def omega_0(x, p):
    if x >= 0 and x < p - 1:
        return x
    else:
        return 0


omega = omega_0


class Phi:
    def phi_by_omega(self):
        phi = [(['z', i + 1], omega(i, self.p)) for i in range(self.p - 1)]
        return phi

    def __init__(self, m_max, p):
        self.p = p
        self.blocks = {}
        for m in range(1, m_max + 1):
            if m in self.blocks:
                continue
            if m == 1:
                self.blocks[1] = self.phi_by_omega()
            if m != 1:
                self.blocks[m] = self.add(self.shift(self.blocks[m - 1]))

    def plus_one(self, y0):
        Y = [y0]

        k = 0
        t = 1
        explode = False
        for digit in y0:
            if digit == 'z' and t > 0:
                explode = True
                break
            t = 0 if (digit + t < self.p) else 1
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
                    digit2 = (digit + t) % self.p
                    t = 0 if (digit + t < self.p) else 1
                    z.append(digit2)
                else:
                    z.append(digit)
            Z.append(z)

        return Z

    def plus_one_to_block(self, block):
        a = self.plus_one(block[0])
        b = []
        for s in a:
            b.append((s, block[1]))
        return b

    def shift(self, f):
        f2 = []
        for block in f:
            b = self.plus_one_to_block(block)
            f2 += b
        return f2

    def add(self, f2):
        f = []
        for block1 in self.blocks[1]:
            for block2 in f2:
                a = intersect(block1[0], block2[0])
                for s in a:
                    f.append((s, block1[1] + block2[1]))
        return f



