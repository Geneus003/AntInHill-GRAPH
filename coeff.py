import MinRoadAlg
import figny

le_road, graph, n = MinRoadAlg.StartProc()
le_road1, graph1, n1 = MinRoadAlg.StartProc()
test = [10000, 0, 0, 0, 0]
j = 0
for a in range(2, 40, 2):
	for b in range(2, 40, 2):
		for k in range(5, 100, 5):
			for e in range(5, 100, 5):
				L = 0
				j +=1
				print("Time:", j, [a/10, b/10, k/10, e/10])
				for i in range(100):
					L += figny.formicaio_main(graph, n, [a/10, b/10, k/10, e/10]) + figny.formicaio_main(graph1, n1, [a/10, b/10, k/10, e/10])
				if abs(L/100 - (le_road + le_road1)) < test[0]:
					test = [abs(L/100 - (le_road + le_road1)), a/10, b/10, k/10, e/10]
					print("Good:", test)
print(test)

