from phi import Phi
from integrate import *
from omegas import *


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


m_max = 10

def check_phi(PHI):
    p = PHI.p
    PHI = PHI.blocks
    for m in range(1, m_max):
        list = integrate(PHI[m], p, mode='list')
        if not is_symmetric(trim(list)):
            print("False for p =", p, "; m =", m)
            break


for p in range(3, 20):
    check_phi(PHI=Phi(m_max, p, omega=step_omega))