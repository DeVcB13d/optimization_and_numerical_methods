'''
Finding an integral using trapezoidal rule

integral (f(x)) a to b = h/2 (f0 + fn + 2*(f1 + f2 + f3 + ... + fn-1))

h = b-a / step_size

fi = f(h*i)

'''

def trapezoidal(f,a,b,step):
    h = (b - a) / step
    # Array to store x_i and y_i values
    x = [i*h + a for i in range(0,step)]
    y = [f(j) for j in x]

    #print(x)
    #print(y)

    # Applying trapezoid formula
    I = y[0] + y[-1]

    # iterating through 1 to n-1
    for i,f_i in enumerate(y[1:-1]):
        I += 2*f_i

    
    I = I*(h/2)

    return I

def main():
    f = lambda x: 2 / (1 + x**3)

    a = 0
    b = 0.8

    steps = 100

    I = trapezoidal(f,a,b,steps)

    print("Integral of f(x) from {0} to {1} is {2}".format(a,b,I))

if __name__ == "__main__":
    main()