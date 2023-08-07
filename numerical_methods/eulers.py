'''
WRITE A PROGRAM TO APPROXIMATE THE SOLUTIONS OF ORDINARY DIFFERENTIAL EQUATIONS USING EULER METHOD

y_n+1 = y_n + h*f(x_n,y_n)

where h = (x_n+1 - x_n) / step
'''

import math

def euler_method(x0,y0,k,step,func):
    x = x0
    y = y0

    h = (k - x0) / step
    print("x = ",x," y = ",y)
    print("h = ",h)
    while x <= k:
        y = y + h*func(x,y)
        x = x + h
        print("x = ",x," y = ",y)
    return y

def main():
    x0 = 0
    y0 = 1
    k = 0.1
    step = 50
    func = lambda x,y: (x**3) * math.exp(-2*x) - y 
    y = euler_method(x0,y0,k,step,func)
    print("y(2) = ",y)

main()