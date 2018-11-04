import MinRoadAlg
import figny

number_graph = 10
number_test = 10000


le_road, graph, n = [], [], []
for i in range(number_graph):
	le_road += [0]
	graph += [0]
	n += [0]
	le_road[i], graph[i], n[i] = MinRoadAlg.StartProc()
le_road_sum = sum(le_road)

Good = [10000, 0, 0, 0, 0]
j = 0

for a in range(1, 45, 1):
	for b in range(1, 45, 1):
		for k in range(1, 100, 1):
			for e in range(1, 100, 1):
				L = 0
				j +=1
				
				print("Time:", j, [a/10, b/10, k/10, e/10])
				
				for i in range(number_test):
					for l in range(number_graph):
						L += figny.formicaio_main(graph[l], n[l], [a/10, b/10, k/10, e/10])
					
				if abs(L/number_test - le_road_sum) < Good[0]:
					Good = [abs(L/number_test - le_road_sum), a/10, b/10, k/10, e/10]
					print("Good:", Good)
				
print(test)
