import numpy as np

def calculate_cost_matrix(distances):
    # Subtract the distances from the maximum distance
    # to convert the problem into a minimization problem
    max_distance = np.max(distances)
    cost_matrix = max_distance - distances
    return cost_matrix

def solve_tsp(distances,min_element = 0):
    cost_matrix = calculate_cost_matrix(distances)
    n = cost_matrix.shape[0]
    
    # Step 1: Subtract the minimum value in each row
    min_rows = np.min(cost_matrix, axis=1)
    for i in range(n):
        cost_matrix[i, :] -= min_rows[i]
    
    # Step 2: Subtract the minimum value in each column
    min_cols = np.min(cost_matrix, axis=0)
    for i in range(n):
        cost_matrix[:, i] -= min_cols[i]
    
    # Step 3: Cover the zeros with the minimum number of lines
    row_covered = np.zeros(n, dtype=bool)
    col_covered = np.zeros(n, dtype=bool)
    
    while True:
        zeros = np.where(cost_matrix == 0)
        row_zeros, col_zeros = zeros[0], zeros[1]
        num_zeros = len(row_zeros)
        
        if num_zeros >= n:
            break
        
        for i in range(num_zeros):
            row = row_zeros[i]
            col = col_zeros[i]
            
            if not row_covered[row] and not col_covered[col]:
                row_covered[row] = True
                col_covered[col] = True
                break
        
        # Step 4: Create additional zeros
        while True:
            cols_covered = np.where(row_covered)[0]
            covered_rows = np.where(col_covered)[0]
            
            if len(cols_covered) + len(covered_rows) >= n:
                break
            
            uncovered_rows = np.where(~row_covered)[0]
            uncovered_cols = np.where(~col_covered)[0]
            min_val = np.min(cost_matrix[uncovered_rows, :][:, uncovered_cols])
            
            for row in uncovered_rows:
                cost_matrix[row, uncovered_cols] -= min_val
            
            for col in uncovered_cols:
                cost_matrix[uncovered_rows, col] -= min_val
        
    # Step 5: Find the optimal assignment
    assignment = np.zeros(n, dtype=int)
    rows, cols = np.where(cost_matrix == 0)
    
    for i in range(len(rows)):
        row, col = rows[i], cols[i]
        
        if assignment[col] == 0:
            assignment[col] = row
    
    return assignment

def is_solution_valid(solution):
    visited_nodes = set()
    for node in solution:
        if node in visited_nodes:
            return False
        visited_nodes.add(node)
    return len(visited_nodes) == len(solution)

# Example usage
# distances = np.array([[0, 2, 9, 10],
#                      [1, 0, 6, 4],
#                      [15, 7, 0, 8],
#                      [6, 3, 12, 0]])
distances =np.array( [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]] )

optimal_order = solve_tsp(distances)
cost = distances[optimal_order, range(distances.shape[1])].sum()
print(optimal_order)
print(cost)