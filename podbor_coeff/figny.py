import graph
import random

def formicaio_main(graph, n, coeff, Qu_ants):
	fero = []
	for i in range(n):
		fero.append([])
		for j in range(n):
			fero[i].append(0)
	for i in range(Qu_ants):
		fero, L = choice_way(graph, n, fero, coeff)
	return(L)
	
# Выбор пути
def choice_way(graph, n, fero, coeff):
	i = 0
	way = [i]
	L = 0
	for x in range(n-1):
		probability = [(fero[i][j])**coeff[0] + (graph[i][j])**(-coeff[1]) for j in range(n)]
		for l in way:
			probability[l] = 0
		sum_ = sum(probability)
		for l in range(n):
			probability[l] /= sum_
		rand = random.random() - 0.00001
		for l in range(n):
			rand -= probability[l]
			if rand < 0:
				i = l
				break
		L += graph[way[x]][i]
		way += [i]
	L += graph[i][0]
	
	d = []
	for l in range(n):
		d.append([])
		for p in range(n):
			d[l].append(0)
	for l in range(len(way)-1):
		d[way[l]][way[l+1]] = coeff[2]/L
		d[way[l+1]][way[l]] = coeff[2]/L
	d[way[0]][way[-1]] = coeff[2]/L
	d[way[-1]][way[0]] = coeff[2]/L
		
	for l in range(n):
		for p in range(n):
			fero[l][p] = coeff[3]*fero[l][p] + d[l][p]
			
	way += [0]
	return(fero, L)
	


if __name__ == "__main__":
	graph, n = graph.generate_graph()
	print(formicaio_main(graph, n, [3.6, 3.8, 0.5, 1.0], 10000))
