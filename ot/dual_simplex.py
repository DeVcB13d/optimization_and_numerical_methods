'''
Approximate steps

1. LPP input in standard form z = [] S.T Ax <= b
2. Construct simplex table
3. Find the leaving vector min(X_b)
4. Find the incoming vector
5. 

'''
import numpy as np
from fractions import Fraction

c = [12, 3, 4, 0, 0]
A = [
    [-4, -2, -3,  1,  0],
    [-8, -1, -2,  0,  1]
]
b = [-2, -3]


'''
Pivot step
In this step, we will perform the pivot operation on the tableau 
to get the next tableau that is closer to the optimal solution.

The pivot operation is performed on the pivot element, which is the
element in the pivot position. The pivot position is the position of
the element with the smallest value in the last row of the tableau.

input: tableau, pivot position
output: new tableau

'''
def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]
    
    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value
    
    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier
   
    return new_tableau

# Converting to tableau
def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

# Checking if the tableau is optimal
def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

# Finding the solution of a given tableau
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


'''
Function to print the simplex table

input: simplex table
output: None
'''
def show_solutions(tableau):
    solutions = get_solution(tableau)
    var = ["x{0}".format(i+1) for i in range(len(tableau)-1)]
    for s,v in zip(solutions,var):
        print("{0} : {1}".format(v,Fraction(str(s)).limit_denominator(100)),end = '\n')
    print("z : {0}".format(Fraction(str(tableau[-1][-1])).limit_denominator(100)))

# Find the rows with negative values in the last column
def can_be_improved_for_dual(tableau):
    rhs_entries = [row[-1] for row in tableau[:-1]]
    return any([entry < 0 for entry in rhs_entries])

#Finding the pivot position
def get_pivot_position_for_dual(tableau):
    rhs_entries = [row[-1] for row in tableau[:-1]]
    min_rhs_value = min(rhs_entries)
    row = rhs_entries.index(min_rhs_value)
    
    columns = []
    for index, element in enumerate(tableau[row][:-1]):
        if element < 0:
            columns.append(index)
    columns_values = [tableau[row][c] / tableau[-1][c] for c in columns]
    column_min_index = columns_values.index(min(columns_values))
    column = columns[column_min_index]

    return row, column


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


def dual_simplex(c, A, b):
    # Conversion to simplex table
    tableau = to_tableau(c, A, b)
    print("initial tableau: ")
    print_table(tableau)
    it = 0
    # While
    while can_be_improved_for_dual(tableau):
        print("\n\nIteration: ",it)
        print_table(tableau)
        it += 1
        pivot_position = get_pivot_position_for_dual(tableau)
        tableau = pivot_step(tableau, pivot_position)

    show_solutions(tableau)
    return get_solution(tableau)

soln  = dual_simplex(c, A, b)
opt = 0

for i in range(len(c)):
    opt += c[i]*soln[i]

print("Optimal solution is: ",opt)



