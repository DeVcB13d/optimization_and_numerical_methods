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
    f = lambda x: 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)

    #f = lambda x: 2 / (1 + x**3)
    a = 0
    b = 0.8

    step = 2

    for step in range(1000,1010):
   
        I = trapezoidal(f,a,b,step)
        print("steps {0}  Integral : {1}".format(step,I))

if __name__ == "__main__":
    main()