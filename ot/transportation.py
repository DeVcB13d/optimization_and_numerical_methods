# Program to implement transportation problem

'''
1. Finding initial feasible solution using north-west corner method

    a) North-West Corner method:
        i) Find the northwest 

'''

import numpy as np


'''
Function to find the northwest corner

input: temp_source temp_dest arrays

returns: row and column value of NW corner
'''
def find_north_west_corner(temp_source,temp_dest):
    for i,s in enumerate(temp_source):
        if ( s != 0 ):
            for j,d in enumerate(temp_dest):
                if ( d != 0 ):
                    return (i,j)

    return False

'''
Function to apply northwest corner method

returns: Matrix of the costs for each cell
'''

def north_west_corner(sources,dest,costs):
    # temp_sources and dests are used to dectement costs
    temp_source = sources.copy()
    temp_dest = dest.copy()
    n_source,n_dests = costs.shape
    # To store assigned costs
    assigned = np.zeros(costs.shape)

    while find_north_west_corner(temp_source,temp_dest):
        x,y = find_north_west_corner(temp_source,temp_dest)
        min_cost = min(temp_source[x],temp_dest[y])
        temp_source[x] -= min_cost
        temp_dest[y] -= min_cost
        assigned[x][y] = min_cost
    return assigned

'''
Function to find cost given the assignments
'''
def get_cost(cost,assigned):
    total_cost = 0
    for c_r,a_r in zip(cost,assigned):
        for c,a in zip(c_r,a_r):
            total_cost+=c*a
    return total_cost



'''
Function to find the u and v values

input: sources,dest,costs,assigned
output: u,v values

This function is used to find the u and v values to find the penalty

'''
def find_uv_values(sources,dest,costs,assigned):
    # Finding u,v values to find the penalty
    U = [None for i in range(len(sources))]
    V = [None for i in range(len(dest))]
    U[0] = 0
    # Variable to check if the V and V columns are filled
    filled = False
    while not filled:
        # Iterating through columns to find Vi's
        for i,row in enumerate(assigned):
            for j,row_el in enumerate(row):
                # Only enter if U_i is assigned
                    if U[i] != None:
                    # If an assigned row
                        if row_el > 0 :
                            # If V is not filled
                            if V[j] == None:
                                # Assign new value for V_i
                                V[j] = costs[i][j] - U[i]
        # Iterating the rows to find U_i's
        assigned_T = np.transpose(np.array(assigned))
        for i,col in enumerate(assigned_T):
            for j,col_el in enumerate(col):
                # Only enter if V_i is assigned
                    if V[i] != None:
                    # If an assigned row
                        if col_el > 0 :
                            # If V is not filled
                            if U[j] == None:
                                # Assign new value for V_i
                                U[j] = costs[i][j] - V[i]
        
        # Checking if u and v are filled
        filled_u = True
        filled_v = True
        for u in U:
            if u == None:
                filled_u == False
        for v in V:
            if v == None:
                filled_v = False
        if filled_u and filled_v:
            filled = True
        else:
            filled = False
    return U,V

'''
Function to find the penalty values
P = u_i + v_j - c_ij

input: U,V,costs
output: penalty value matrix
'''   
def get_penalties(U,V,cost,assigned):
    penalty = np.zeros(cost.shape)
    for i,u in enumerate(U):
        for j,v in enumerate(V):
            if assigned[i][j] == 0:
                penalty[i][j] = u+v-cost[i][j]
    return penalty

'''
Function to check if the given penalty matrix is optimal

input: penalty matrix
output: True if optimal else False
'''
def check_optimality(penalty):
    for row in penalty:
        for el in row:
            if el > 0:
                return False
    return True

'''
Finding the entering variable which has the maximum penalty
input: penalty matrix
'''
def get_entering_variable_position(penalty):
    penalty_copy = np.array(penalty)
    penalty_copy = penalty_copy.flatten()
    penalty_copy = np.sort(penalty_copy)
    position = np.where(penalty == penalty_copy[-1])
    return int(position[0]),int(position[1])

def get_next_cells(matrix, position):
    x,y = position
    next_cells = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    next_cells = [
                    cell for cell in next_cells if 
                    cell[0] >= 0 
                    and cell[1] >= 0 
                    and cell[0] < matrix.shape[0] 
                    and cell[1] < matrix.shape[1] 
                    and matrix[cell[0], cell[1]] != 0
                ]
    return next_cells

    
'''
Function to find the closed loop to be pivoted

input: cost,assigned,entering_variable

'''

def find_closed_loop(assigned, start, visited, path, check = 0):
    i, j = start
    visited[i, j] = 1

    next_cells = get_next_cells(assigned, start)
    for cell in next_cells:
        if visited[cell[0], cell[1]] == 0:
            if cell in path:
                return path
            else:
                visited[cell[0], cell[1]] = 1
                result = find_closed_loop(assigned, cell, visited, path + [cell],check+1)
                if result is not None:
                    return result
        elif check >= 2:
            return path


def get_closed_loop(assigned, start):
    visited = np.zeros(assigned.shape)
    path = [start]
    final_path = find_closed_loop(assigned, start, visited, path)
    return final_path

'''
Function to find the pivot cell 
'''
def pivoting(cost,assigned,closed_loop):
    # Finding the pivot cell
    pivot_cell = closed_loop[1]
    assigned_copy = np.array(assigned)
    pivot_cost = assigned[pivot_cell[0],pivot_cell[1]]
    for i in range(len(closed_loop)):
        cell = closed_loop[i]
        if i%2 == 0:
            assigned_copy[cell[0],cell[1]] += pivot_cost
        else:
            assigned_copy[cell[0],cell[1]] -= pivot_cost
    return assigned_copy

def display_results(cost_matrix, allocations, u_values, v_values):
    num_sources, num_destinations = cost_matrix.shape
    # Display the cost matrix
    print("Cost Matrix:")
    for i in range(num_sources):
        for j in range(num_destinations):
            print("{:<5}".format(cost_matrix[i, j]), end=" ")
        print()

    print()

    # Display the assigned values
    print("Assigned Values:")
    for i in range(num_sources):
        for j in range(num_destinations):
            print("{:<5}".format(allocations[i, j]), end=" ")
        print()

    print()

    # Display the u values
    print("U Values:")
    for i in range(num_sources):
        print("U[{}]: {}".format(i, u_values[i]))

    print()

    # Display the v values
    print("V Values:")
    for j in range(num_destinations):
        print("V[{}]: {}".format(j, v_values[j]))

    print()
'''
Program to apply Modi method to find optimal solution
1. Find u,v values
2. 
'''
def Modi_method(sources,dest,costs):
    # Getting the intial feasibl solution
    assigned  = north_west_corner(sources,dest,costs)
    print("initial assigned values : \n",assigned)
    print("initial cost: ",get_cost(costs,assigned))
    # Defining penalty P 
    P = lambda u,v,c : u+v-c
    # Finding u and v values
    U,V = find_uv_values(sources,dest,costs,assigned)
    print("Initial U values: ",U)
    print("Initial V values: ",V)
    # Finding the penalty matrix
    penalty = get_penalties(U,V,costs,assigned)
    print("Initial Penalty matrix: \n",penalty)
    # Checking if the penalty matrix is optimal
    while not check_optimality(penalty):
        start = get_entering_variable_position(penalty)
        loop = get_closed_loop(assigned,start)
        assigned = pivoting(costs,assigned,loop)
        U,V = find_uv_values(sources,dest,costs,assigned)
        penalty = get_penalties(U,V,costs,assigned)
        display_results(costs,assigned,U,V)

    print("Final assigned values : \n",assigned)
        

    
if __name__ == "__main__":
    # input datas

    sources = np.array([250,350,400])
    dest = np.array([200,300,350,150])

    costs = np.array([
            [3,1,7,4],
            [2,6,5,9],
            [8,3,3,2]
        ])

    Modi_method(sources,dest,costs)