# Program to perform simplex method in python


import math
import numpy as np
from fractions import Fraction



# Convertion into tableau

def to_tableau(z,A,b):
    # Augmenting A and b
    tableau = [eq + [x] for eq, x in zip(A, b)]
    # Adding 0 to make z size compatible to A|b
    z = z + [0]
    #Adding z as the final row
    tableau += [z]
    return tableau

# Function to print tableau
def print_table(tableau):
    n_var = len(tableau[0])
    var = ["x{0}".format(i+1) for i in range(n_var-1)]
    for j in var:
        print(j,end = '\t')
    print("c ",end = '\n\n')
    
    for k in tableau:
        for eq in k:
            print(Fraction(str(eq)).limit_denominator(100), end ='\t')
        print('\n')

# Function to check for optimality
def is_optimal(tableau):
    # Optimality is reached only when z < 0 
    z = tableau[-1]
    # z[-1] always equals 0
    # any() would return a boolean value
    return not any(i > 0 for i in z[:-1])

# Function to find pivot element
def find_pivot_element(tableau):
    '''
    pivot column (pc) is the maximum value of z 
    pivot row (pr) is the min of ratios of b values with pivot column values
    pr = index(min( [ b[i] / pc[i] ])) 
    '''
    z = tableau[-1]
    ipc = next(i for i, x in enumerate(z[:-1]) if x > 0)
    ratio = []
    for eq in tableau[:-1]:
        el = eq[ipc]
        ratio.append(math.inf if el < 0 else eq[-1] / el)
    ipr = ratio.index(min(ratio))
    return ipr,ipc

        
def pivot_step(tableau,pivot_position):
    # finding zj
    new_tableau = [[] for i in tableau]
    ipr,ipc = pivot_position
    pivot_element = tableau[ipr][ipc]
    # Dividing the pivot row by pivot element
    new_tableau[ipr] = [el/pivot_element for el in tableau[ipr]]
    # Changing the other rows
    for eq_i,eq in enumerate(tableau):
        if eq_i != ipr:
            new_tableau[eq_i] = [
                tableau[eq_i][i] - new_tableau[ipr][i] * tableau[eq_i][ipc]
                for i in range(len(new_tableau[ipr]))
                ]
    return new_tableau
    

def simplex(z,A,b):
    # Converting the equations to tableau
    tableau = to_tableau(z,A,b)
    print("initial tableau\n\n")
    print_table(tableau)
    find_pivot_element(tableau)
    it = 1
    while not is_optimal(tableau):
        pivot_position = find_pivot_element(tableau)
        tableau = pivot_step(tableau,pivot_position)
        print('\n\niteration: {0}\n'.format(it))
        print_table(tableau)
        it+=1
    return tableau
        

def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
    return solutions

def show_solutions(tableau):
    solutions = get_solution(tableau)
    var = ["x{0}".format(i+1) for i in range(len(tableau)-1)]
    for s,v in zip(solutions,var):
        print("{0} : {1}".format(v,Fraction(str(s)).limit_denominator(100)),end = '\n')
    print("z : {0}".format(Fraction(str(tableau[-1][-1])).limit_denominator(100)))

def main():
    
    '''
    Consider the LPP

    maximize z = 12x1 + 16x2
    ST:
    1) 10x1 + 20x2 + x3 = 120
    2)  8x1 +  8x2 + x4 = 80
    3)  x1,x2,x3,x4 > 0
    '''
    z = [2,-3,6,0,0,0]
    A = [
            [ 3,-1, 2, 1, 0, 0],
            [-2,-4, 0, 0, 1, 0],
            [-4, 3, 8, 0, 0, 1]
        ]
    b = [ 7,12,10]
    show_solutions(simplex(z,A,b))

if __name__ == "__main__":
    main()






