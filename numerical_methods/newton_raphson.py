# Finding roots using newton-raphson method

import math

def newton_raphson(function,derivative_function,coefficients =None,powers =None,interval=None,prescision = 0.01):
    # Defining the function
    x_next = lambda x : x - function(x)/derivative_function(x)
    if interval:
        x = interval[0]
    else:
        x = 1
    iter = 0
    while abs(function(x)) > prescision:
        x = x_next(x)
        print("Iteration: ",iter," x:",x)
        iter+=1
    return x


def main():
    # coefficients = eval(input("Enter the coefficients: "))
    # powers = eval(input("Enter the powers: "))
    # interval = eval(input("Enter the interval: "))
    #coefficients = [1,-1,2] 
    #powers = [3,2,0]
    #interval = [1,10]  
    function = lambda x : x**3 - 12
    derivative_function = lambda x : 3*x**2
    res = newton_raphson(function,derivative_function)
    print("The root is: ",res)

main()