import MinRoadAlg
import figny
rezult = 0
r = 0
odin = 0
dva = 0
for i in range(1000):
	le_road, graph, n = MinRoadAlg.StartProc()
	L = figny.formicaio_main(graph, n, [3.6, 3.8, 0.5, 1.0])
	rezult += L - le_road
	if L == le_road:
		r += 1
	if round((L - le_road) / le_road, 2) == 0.01:
		odin += 1
	if round((L - le_road) / le_road, 2) == 0.02:
		dva += 1
	print(i)
print(rezult / 1000, r, odin, dva)
