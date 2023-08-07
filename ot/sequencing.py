# Script to solve sequencing problem

import numpy as np

# Converting to 2 machine problem


def check_solvability(table):
    # Check if table is solvable

    # Finding minimum values of first and last rows
    min_M1 = np.min(table[:, 0])
    min_Mk = np.min(table[:, -1])
    max_mid = []
    # Finding maximum values of middle rows
    for row in table[:, 1:-1]:
        max_Mi = np.max(row)
        max_mid.append(max_Mi)

    # Checking if table is solvable
    C1 = True
    for elem in max_mid:
        if elem > min_M1:
            C1 = False
    C2 = False
    for elem in max_mid:
        if elem > min_Mk:
            C2 = False
    return C1 or C2


# returning the sum of middle elements in the machine
def middle_machine_sum(table):
    sum_table = np.zeros(len(table[0]))
    for row in table[:, 1:-1]:
        for i, elem in enumerate(row):
            sum_table[i] += elem
    return sum_table


# Function to convert a K machine problem to 2 machine
def convert_to_2_machines(table):
    # Check if middle elements have a constant sum
    mid_sum = middle_machine_sum(table)
    C = mid_sum[0]
    constant_sum = True
    for elem in mid_sum:
        if elem != C:
            constant_sum = False
            break
    new_table = []
    # In case of middle rows having a constant sum
    # Choose M1 and Mk
    if constant_sum:
        new_table.append(table[0])
        new_table.append(table[-1])
        return np.array(new_table)
    else:
        # if not a a constant sum add the middle sums to row 1 and row k
        H = [k1 + j for k1, j in zip(mid_sum, table[0])]
        G = [k2 + j for k2, j in zip(mid_sum, table[-1])]
        new_table.append(H)
        new_table.append(G)
        return np.array(new_table)


# Function to assign sequences
def sequence_assign(seq_table):
    if len(seq_table)  != 2:
        seq_table = convert_to_2_machines(seq_table)
    print("seq_table", seq_table)
    # Array to store  zeros
    assign = np.zeros(len(seq_table[0]))
    # Array to mark assignments
    marked = np.zeros([2,len(seq_table[0])])

    # Indexes for the machines
    i_H = 0
    i_G = -1

    # Repeating until all elements are assigned
    while (np.sum(marked) / 2) != len(seq_table[0]):
        # finding the minimum unmarked element in seq_table
        print("marked",marked)
        print("zeros",np.min(seq_table[marked == 0]))
        print(seq_table)

        min_index = np.where(seq_table == (np.min(seq_table[marked == 0])))
        print("min_index", seq_table[marked == 0])
        print("min_index", min_index)
        # If only one minimum element
        if len(min_index[1]) == 1:
            # If in first row
            if min_index[0][0] == 0:
                assign[i_H] = min_index[1][0]
                marked[0,min_index[1][0]] = 1
                marked[1,min_index[1][0]] = 1
                i_H += 1
            # If in last row
            elif min_index[0][0] == 1:
                assign[i_G] = min_index[1][0]
                marked[0,min_index[1][0]] = 1
                marked[1,min_index[1][0]] = 1
                i_G -= 1
        # If more than one minimum element
        else:
            # case 1: If minimum elements are in the same row
            if min_index[0][0] == min_index[0][1]:
                # Finding the minimum cost in second row
                if seq_table[min_index[0][1],min_index[1][1]] < seq_table[min_index[0][0],min_index[1][0]]:
                    assign[i_G] = min_index[1][1]
                    marked[0,min_index[1][1]] = 1
                    marked[1,min_index[1][1]] = 1
                    i_G -= 1
                else:
                    assign[i_H] = min_index[1][0]
                    marked[0,min_index[1][0]] = 1
                    marked[1,min_index[1][0]] = 1
                    i_H += 1
            # case 2: If minimum elements are in different rows
            else:
                assign[i_H] = min_index[1][0]
                assign[i_G] = min_index[1][1]
                marked[0,min_index[1][0]] = 1
                marked[1,min_index[1][1]] = 1
                i_H += 1
                i_G -= 1
    return assign, marked


def main():
    # Array describin costs and machines
    table = np.array(
        [[2,5,4,9,6,8,7,5,4],[6,8,7,4,3,9,3,8,11]]
    )
    #table =np.array([[1,5,4,9,6,8,7,5,4],[6,8,7,4,3,9,3,8,11]])
    # Assigning sequences
    assign, marked = sequence_assign(table)
    print("Assignments : ", assign)
    print("Marked : ", marked)


if __name__ == "__main__":
    main()
