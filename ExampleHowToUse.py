import graph

matrix, n = graph.generate_graph()

for i in range(n):
    print()
    for j in range(n):
        print(matrix[i][j], " ", end="")