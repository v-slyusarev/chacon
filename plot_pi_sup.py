from phi import *
from intersect import *
from integrate import *
from omegas import *
import numpy as np
from matplotlib import pyplot

p=3

PHI = Phi(1000, p).blocks
sup_list = [float(np.max(integrate(PHI[key], p, mode='list'))) for key in PHI]

pyplot.figure(figsize=(40, 20))
pyplot.plot(sup_list)
pyplot.savefig('sup{}.png'.format(p))