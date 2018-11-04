import MinRoadAlg
import figny

def test_coeff(coeff):
	percent = {}
	
	for i in range(1000):
		le_road, graph, n = MinRoadAlg.StartProc()
		L = figny.formicaio_main(graph, n, coeff)
		
		percent_temp = round(abs((L - le_road)/le_road), 2)
		if percent.get(percent_temp) == None:
			percent[percent_temp] = 1
		else:
			percent[percent_temp] += 1
	
	percent = sorted(percent.items())
	return(percent)
	
if __name__ == "__main__":
	print(test_coeff([3.6, 3.8, 0.5, 1.0]))

