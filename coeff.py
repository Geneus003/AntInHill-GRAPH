import MinRoadAlg
import figny

le_road, graph, n = MinRoadAlg.StartProc()
test = [1000, 0, 0, 0, 0]
j = 0
for a in range(2, 40, 2):
	for b in range(2, 40, 2):
		for k in range(5, 100, 5):
			for e in range(5, 100, 5):
				L = 0
				j +=1
				print("Time:", j, [a/10, b/10, k/10, e/10])
				for i in range(50):
					L += figny.formicaio_main(graph, n, [a/10, b/10, k/10, e/10])
				if abs(L/5 - le_road) < test[0]:
					test = [abs(L/5 - le_road), a/10, b/10, k/10, e/10]
					print("Good:", test)
print(test)
