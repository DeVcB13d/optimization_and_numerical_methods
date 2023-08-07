'''
Program to solve assignment problem using hungarian algorithm
'''

import numpy as np

'''
To reduce smallest element from each row and column
'''
def reduction(cost):

    num_rows, num_columns = cost.shape
    # Reducing from rows
    for i,row in enumerate(cost):
        min_el = np.min(row)
        for j,el in enumerate(row):
            cost[i][j] -= min_el
    # Reducing from columns
    for k in range(num_columns):
        # getting kth column
        column = cost[:,k]
        min_el = np.min(column)
        for l in range(num_rows):
            cost[l][k] -= min_el
    return cost

'''
function to perform assignment given reduced cost matrix
'''
def assignment(cost):
    # assignment Matrix with cross and circles
    # CROSS = -1 denotes unassigned 0
    # CIRCLE = 1 denotes an assigned 0
    assigned = np.zeros(cost.shape)
    # Traverse via rows
    for i,row in enumerate(cost):
        zeros = np.where(row == 0)
        assigned_row = assigned[i,:]
        unmarked = False
        # Check for single unmarked zero
        for z in zeros[0]:
            if assigned_row[z] == 0:
                unmarked = True
        if unmarked or len(zeros[0]) == 1:
            # assign the 0
            assigned[i,zeros[0][0]] = 1
            # Selecting column with the 0
            column = cost[:,zeros[0][0]]
            # Select zeros in the column
            col_zeros = np.where(column == 0)
            # Cross the remaining zeros in the column
            for index in col_zeros[0]:
                if index != i:
                    assigned[index,zeros[0][0]] = -1
    # Traverse via columns
    num_rows, num_columns = cost.shape
    for j in range(num_columns):
        column = cost[:,j]
        zeros = np.where(column == 0)
        assigned_column = assigned[:,j]
        unmarked = False
        # Check for single unmarked zero
        for z in zeros[0]:
            if assigned_column[z] == 0:
                unmarked = True
        if unmarked or len(zeros[0]) == 1:
            # assign the 0
            assigned[zeros[0][0],j] = 1
            # Selecting row with the 0
            row = cost[zeros[0][0],:]
            # Select zeros in the row
            row_zeros = np.where(row == 0)
            # Cross the remaining zeros in the row
            for index in row_zeros[0]:
                if index != j:
                    assigned[zeros[0][0],index] = -1
    return assigned
'''
Function to check if the assignment is optimal

It checks if all the rows and columns have been assigned
'''

def is_optimal(assigned):
    num_assigned = np.where(assigned == 1)
    if len(num_assigned[0]) == assigned.shape[0]:
        return True
    else:
        return False        
            
'''
Function to mark matrix to get minimal lines via all zeros

marking conditions:
1. If a row has no assigned zeros, mark the row
2. columns with 0 in the marked rows, mark the column
3. rows with assigned 0 in the marked columns, mark the row
'''
def mark_assigned_martrix(assigned):   
    mark_row = np.zeros(assigned.shape[0])
    mark_column = np.zeros(assigned.shape[1])
    # Marking rows without assigned zeros
    for i,row in enumerate(assigned):
        zeros = np.where(row == 1)
        if len(zeros[0]) == 0:
            mark_row[i] = 1
    # Marking columns with zeros in marked rows
    for j,mark in enumerate(mark_row):
        # in case of a marked row
        if mark == 1:
            row = assigned[j]
            for r,el in enumerate(row):
                # presence of 0
                if el == 1 or el == -1:
                    mark_column[r] = 1
    # Marking rows with assigned 0 in the marked columns
    for k,mark in enumerate(mark_column):
        # if a marked column
        if mark == 1 :
            column = assigned[:,k]
            for c,mark in enumerate(column):
                # in the case of an assigned 0
                if mark == 1:
                    mark_row[c] = 1
    return mark_row,mark_column

'''
Function to find a new cost matrix given the marked rows and columns

Lines are drawn via unmarked rows and marked columns
1. Find smallest element in the non covered elements
2. Subtract the smallest element from all non covered
3. Add it to interesecting lines
'''
def get_new_cost_matrix(cost,assigned,mark_row,mark_column):
    line_column = mark_column.copy()
    line_row = mark_row.copy()
    # unmarked rows
    line_row = 1 - line_row
    # Finding the smallest uncovered element
    uncovered = []
    for i,row in enumerate(assigned):
        for j,col in enumerate(row):
            if line_column[j] != 1 and line_row[i] != 1:
                uncovered.append(cost[i][j])
    min_el = min(uncovered)
    # Subtracting and adding min_el
    for i,row in enumerate(cost):
        for j,col in enumerate(row):
            if line_column[j] != 1 and line_row[i] != 1:
                cost[i][j] -= min_el
            elif line_column[j] == 1 and line_row[i] == 1:
                cost[i][j] += min_el
    return cost
'''
Function to get the final solution given assignment matrix

'''
def get_solution(assigned):
    solution = []
    for i,row in enumerate(assigned):
        for j,col in enumerate(row):
            if col == 1:
                solution.append((i,j))
    return solution

# To print the matrix
def print_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print("{:<5}".format(matrix[i, j]), end=" ")
        print()
'''
Hungarian assignment

input: cost 2x2 array
output: assigned elements
'''
def hungarian_assignment(cost):
    print("Initial cost :\n ")
    print_matrix(cost)
    cost = reduction(cost)
    print("\nReduced Cost: \n")
    print_matrix(cost)
    assigned = assignment(cost)
    print("\nIntitial assignement: \n")
    print_matrix(assigned)
    iteration = 0
    # Iterating till optimality is reached
    while not is_optimal(assigned):
        print("\n\niteration {0}".format(iteration))
        print("\nNot optimal")
        # Marking rows and columns
        mark_row, mark_column = mark_assigned_martrix(assigned)
        print("\nMarked rows: ",mark_row)
        print("\nMarked columns: ",mark_column)
        # Getting new cost matrix usign marked rows and columns 
        cost = get_new_cost_matrix(cost,assigned,mark_row,mark_column)
        print("\nNew cost : \n")
        print_matrix(cost)
        # Assigning again for the new cost matrix
        assigned = assignment(cost)
        print("\nNew assignment: \n")
        print_matrix(assigned)
        iteration += 1
    # Getting the solution
    print("Optimality reached")
    print("\nFinal assigned matrix: \n")
    print_matrix(assigned)
    solution = get_solution(assigned)
    print("Solution: ",solution)

if __name__ == "__main__":
    cost = np.array([
        [85, 75, 65, 125, 75],
        [90, 78, 66, 132, 78],
        [75, 66, 57, 114, 69],
        [80, 72, 60, 120, 72],
        [76, 64, 56, 112, 68]
    ])
    hungarian_assignment(cost)
    print("Done!")