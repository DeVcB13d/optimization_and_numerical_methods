'''
WRITE A PROGRAM TO ESTIMATE THE VALUE OF A FUNCTION FOR ANY INTERMEDIATE VALUE 
OF THE INDEPENDENT VARIABLE USING NEWTON FORWARD INTERPOLATION METHOD

1. Table given
    x    3   5   7   9
    f(x) 180 150 120 90

    finding f(k) by forward interpolation

    k = 4

    h = x[0] - x[1] = 3 - 5 = -2

2. Formula
    f(k) = f(x0) + (k-x0)/h * delta_f(x0) + (k-x0)(k-x1)/h^2 * delta^2_f(x0) + ... + (k-x0)(k-x1)...(k-xn-1)/h^n * delta^n_f(x0)    
'''
import math

# calculating the forward difference table
# forward difference
# del_fx = f_x(i+1) - f_x(i) 
def forward_difference_table(x,f_x):
    fd_table = []
    fd_table.append(f_x)
    n = len(x)
    for i in range(n):
        fd_table.append([])
        for j in range(n-i-1):
            delta = fd_table[i][j+1] - fd_table[i][j]
            fd_table[i+1].append(delta)

    return fd_table

def find_previous_x(x,k):
    for i,x_i in enumerate(x):
        if k <= x[i+1] and k > x[i]:
            return x_i , i
    return -1,-1

    
def newtons_forward_interpolation(x,f_x,k):
    # calculating forwarddifference table
    fd_table = forward_difference_table(x,f_x)

    # interval h 
    h = x[0] - x[1]

    # previous x value before k
    x_p, i_x_p= find_previous_x(x,k)

    # finding u 
    u = ( x_p - k ) / h

    # implementation of formula f(k)
    f_k = fd_table[0][i_x_p]
    for i in range(1,len(x)-i_x_p):
        U = 1
        for j in range(i):
            U = U * (u - j)
        U = U/math.factorial(i)
        U = U*fd_table[i][i_x_p]
        #print("{0} term : {1}".format(i,U))
        f_k+=U
    return f_k
            
    
def main():
    x = eval(input("Enter the values of x: "))
    f_x = eval(input("Enter the values of f(x): "))
    k = eval(input("Enter the value of k: "))
    f_k = newtons_forward_interpolation(x,f_x,k)
    print("f({0}) = {1}".format(k,f_k))
    

main()
    
            
