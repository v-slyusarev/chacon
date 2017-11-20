from phi import *
from intersect import *
from integrate import *

def triangle(p):
    n = p - 2
    return n * (n + 1) // 2
'''
PHI = Phi(18, p).blocks
for key in PHI:
    print(key, ':', integrate(PHI[key], p, mode='polynomial'), '\n')

'''
#print(triangle(7))

for p in range(3, 50):
    PHI = Phi(p,  p).blocks
    list1 = integrate(PHI[1], p, mode='list')
    list2 = integrate(PHI[p], p, mode='list')
    print(p, len(list2) - len(list1) == triangle(p))