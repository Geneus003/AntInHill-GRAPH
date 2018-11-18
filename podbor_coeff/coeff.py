import perebor
import figny
import graph

Qu_matrix = 100
Qu_test = 10000


le_road, matrix, n = [], [], []
for i in range(Qu_matrix):
	le_road += [0]
	matrix += [0]
	n += [0]
	matrix[i], n[i] = graph.generate_graph()
	le_road[i], rfrfrfrfrffrfrfrfrfiighyivuguivgukguiyv = perebor.mainus(matrix[i], n[i])
	print(i)
le_road_sum = sum(le_road)

Good = [88005553535, 0, 0, 0, 0]
j = 0

for a in range(25, 45, 1):
	for b in range(25, 45, 1):
		for k in range(1, 100, 1):
			for e in range(1, 100, 1):
				L = 0
				j +=1
				
				print("Time:", j, [a/10, b/10, k/10, e/10])
				
				for i in range(Qu_test):
					print(i)
					for l in range(Qu_matrix):
						L += figny.formicaio_main(matrix[l], n[l], [a/10, b/10, k/10, e/10])
					
				if abs(L/Qu_test - le_road_sum) < Good[0]:
					Good = [abs(L/nQu_test - le_road_sum), a/10, b/10, k/10, e/10]
					print("Good:", Good)
				
print(test)
