from phi import *
from intersect import *
from integrate import *

p=5
PHI = Phi(5, p).blocks
for key in PHI:
    print(key, ': ', PHI[key], '\n', integrate(PHI[key], p, mode='polynomial'), '\n')