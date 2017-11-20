from phi import Phi
from integrate import *
from omegas import square_omega


def trim(list):
    i = 0
    while list[i] == 0:
        i += 1
    return list[i:]

def is_symmetric(list):
    n = len(list) // 2
    for i in range(n):
        if(list[i] != list[len(list) - i - 1]):
            return False
    return True
for p in range(3, 100):
    PHI=Phi(10, p, omega=square_omega).blocks
    for m in range(1, 10):
        list = integrate(PHI[m], p, mode='list')
        if not is_symmetric(trim(list)):
            print("False for p =", p, "m =", m)
    print('checked for p = ', p)