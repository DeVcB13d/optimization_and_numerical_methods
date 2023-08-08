from sys import maxsize
from itertools import permutations
V = 4

def tsp(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_cost = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = s
        for j in i:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][s]
    min_cost = min(min_cost, current_cost)
    return min_cost , vertex

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
distances = [[0, 2, 9, 10],
             [1, 0, 6, 4],
             [15, 7, 0, 8],
             [6, 3, 12, 0]
             ]
s = 0
min_cost,vertex = tsp(distances, s)
print(min_cost)

print("Path: 0",end=" ")
for i in vertex:
    print(i,end=" ")