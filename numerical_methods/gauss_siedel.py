# Program to perform gauss siedel

import numpy as np

def gauss_siedel(A,b):
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    for iter in range(0,5):  
        for i in range(0,n):
            sum = b[i]
            for j in range(0,n):
                if i != j:
                    sum = sum - A[i,j] * x[j]
            x_new[i] = sum / A[i,i]
            x[i] = x_new[i]
        for i in x:
            print("{:.4f}".format(i),end=" ")
        print()
    return x
def main():
    A = np.array([[12,3,-5],[1,5,3],[3,7,13]])
    b = np.array([1,28,76])
    x = gauss_siedel(A,b)
    print("x\n",x)

main()