'''
Program to find roots using bisection method

Expression x**3 - 2*x - 5 = 0
given as 
coefficients = [1,2,-5] 
powers = [3,1,0]
interval = [1,2]  
'''
import math

def bisection(function,coefficients =None,powers =None,interval=None,prescision = 0.01):
    # finding the starting interval
    if not function:
        f = lambda x: (sum(coefficients[i]*x**powers[i] for i in range(len(coefficients))))
    else:
        f = function
    for i in range(interval[0],interval[1]):
        if f(i) > 0:
            a = i-1
            b = i
            break
            # performing bisection
    iter = 0
    while abs(b-a) > prescision:
        c = (a+b)/2
        if f(c) > 0:
            b = c
        else:
            a = c
        print("Iteration: ",iter,"a:",a," b:",b," c:",c)
        iter+=1
    return a

def main():
    # coefficients = eval(input("Enter the coefficients: "))
    # powers = eval(input("Enter the powers: "))
    # interval = eval(input("Enter the interval: "))
    coefficients = [1,-1,2] 
    powers = [3,2,0]
    interval = [1,10]  
    function = lambda x : math.log(x) - 1
    res = bisection(function,coefficients,powers,interval)
    print("The root is: ",res)

main()