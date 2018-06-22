from phi import *
from intersect import *
from integrate import *

p=4
PHI = Phi(10, p).blocks
for key in PHI:
    print(key, ': \n', PHI[key], '\n================================\n')