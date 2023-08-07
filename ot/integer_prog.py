'''
Performing integer programming
'''

from simplex import *

import numpy as np

z = np.array([5,7])
A = np.array([[-2,3],[6,1]])
b = np.array([6,30])

# Finding the initial optimal solution by using simplex method

tableau = simplex(z,A,b)
