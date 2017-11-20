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


def check_phi(PHI):
    p = PHI.p
    PHI = PHI.blocks
    for m in range(1, 10):
        list = integrate(PHI[m], p, mode='list')
        if not is_symmetric(trim(list)):
            print("False for p =", p, "; m =", m)
            break

print('checking omega(x) = x * (p - x - 1)')

for p in (3, 5, 7, 11):
    check_phi(PHI=Phi(10, p, omega=square_omega_1))

print('checking omega(x) = x * (p - x)')

for p in (3, 5, 7, 11):
    check_phi(PHI=Phi(10, p, omega=square_omega_2))

print('checking omega(x) = x^2')

for p in (3, 5, 7, 11):
    check_phi(PHI=Phi(10, p, omega=square_omega_3))
