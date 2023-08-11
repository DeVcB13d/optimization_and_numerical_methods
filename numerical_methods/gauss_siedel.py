# Program to perform gauss siedel

import numpy as np

def gauss_siedel(A,b,its=5):
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    for iter in range(0,its):  
        for i in range(0,n):
            sum = b[i]
            for j in range(0,n):
                if i != j:
                    sum = sum - A[i,j] * x[j]
            x_new[i] = sum / A[i,i]
            x[i] = x_new[i]
        print("iteration : ",iter+1)
        iter += 1
        for i in x:
            print("{:.4f}".format(i),end=" ")
        print()
    return x
def main():
    A = eval(input("Enter the matrix: "))
    b = eval(input("Enter the vector: "))
    A = np.array(A)
    b = np.array(b)
    x = gauss_siedel(A,b,10)
    print("x\n",x)

main()