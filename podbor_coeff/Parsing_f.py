import sys


def parser(con):
	sys.stdin = open("graph_with_len.txt", "r")

	for i in range(con):
		a = input()

	a = input()
	a, b, c = a.split(" ")
	a = int(a)
	b = int(b)
	c = float(c)
	matrix = []

	for i in range(a):
		g = input()
		matrix.append(g.split(" "))
		for j in range(a):
			matrix[i][j] = int(matrix[i][j])

	return a, b, c, matrix
