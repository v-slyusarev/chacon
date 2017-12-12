from phi import Phi
from integrate import *
from omegas import *
from sys import exit

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
            return False

    return True

count=0
while True:
    for j in range(1, 100):
        p = 2 * j + 1
        omega = generate_omega_for_l4(p)
        PHI = Phi(20, p, omega=omega)
        if not check_phi(PHI):
            print(p, "   :   ", [omega(x,p) for x in range(p-1)])
            exit(0)

    count += 1
    if(count % 100 == 0):
        print('checked for ', count, 'random omegas and still true')