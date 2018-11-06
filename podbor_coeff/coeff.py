import perebor
import figny
import graph

number_matrix = 10
number_test = 10000


le_road, matrix, n = [], [], []
for i in range(number_matrix):
	le_road += [0]
	matrix += [0]
	n += [0]
	matrix[i], n[i] = graph.generate_graph()
	le_road[i] = perebor.mainus(matrix[i], n[i])
le_road_sum = sum(le_road)

Good = [100000000, 0, 0, 0, 0]
j = 0

for a in range(1, 45, 4):
	for b in range(1, 45, 4):
		for k in range(1, 100, 5):
			for e in range(1, 100, 5):
				L = 0
				j +=1
				
				print("Time:", j, [a/10, b/10, k/10, e/10])
				
				for i in range(number_test):
					for l in range(number_matrix):
						L += figny.formicaio_main(matrix[l], n[l], [a/10, b/10, k/10, e/10])
					
				if abs(L/number_test - le_road_sum) < Good[0]:
					Good = [abs(L/number_test - le_road_sum), a/10, b/10, k/10, e/10]
					print("Good:", Good)
				
print(test)
