# Program to perform gauss elimination

import numpy as np

def gauss_elimination(A,b):
    n = len(A) 
    for i in range(0,n):
        for j in range(i+1,n):
            print(A)
            try:
                factor = A[i,i] / A[j,i]
                print(A[j,i])
                print("factor : ",factor)
            except ZeroDivisionError:
                print("Division by zero")
                break
            for k in range(0,n):
                A[j,k] = A[j,k] - A[i,k] / factor
            b[j] = b[j] - b[i] / factor
    return A,b

def back_substitution(A,b):
    n = len(A)
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum = b[i]
        for j in range(i+1,n):
            sum = sum - A[i,j] * x[j]
        x[i] = sum / A[i,i]
    return x

def main():
    A = eval(input("Enter the matrix: "))
    b = eval(input("Enter the vector: "))
    A = np.array(A)
    b = np.array(b)
    A,b = gauss_elimination(A,b)
    x = back_substitution(A,b)
    for i in x:
        print("{:.4f}".format(i),end=" ")

main()