import numpy as np
import math
def monte_carlo_volume(r,iter = 100):
    count = 0
    for i in range(iter):
        x = np.random.rand(r)
        y = np.random.rand(r)
        z = np.random.rand(r)
        if np.cbrt(sum(x**2 + y**2 + z**2)) <= r**3:
            count += 1

    return count/iter

if __name__ == '__main__':
    r = 1
    V = math.pi * 4/3
    V = V / ((2*r)**3)
    print('Volume ratio of sphere is {0}'.format(V))
    for i in range(1,7):
        print('Volume of sphere is {0}'.format(monte_carlo_volume(r,10**i)))