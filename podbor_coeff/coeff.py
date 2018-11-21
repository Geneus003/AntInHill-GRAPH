import figny
import Parsing_f


Qu_test = 100

con = 0
pr = 0
n, le_road, t, matrix = [], [], [], []
for i in range(500):
	n_, le_road_, t_, matrix_ = Parsing_f.parser(con + pr)
	
	n += [n_]
	le_road += [le_road_]
	t += [t_]
	matrix += [matrix_]
	pr += n_ + 2

Good = [88005553535, 0, 0, 0, 0]
j = 0

for a in range(1, 50, 1):
	for b in range(1, 50, 1):
		for k in range(5, 1000, 5):
			for e in range(5, 1000, 1):
				L = 0
				j +=1
				
				print("Time:", j, [a/10, b/10, k/10, e/10])
				
				
				for i in range(Qu_test):
					print(i)
					for l in range(500):
						L += figny.formicaio_main(matrix[l], n[l], [a/10, b/10, k/10, e/10]) - le_road[l]
					
				if abs(L/Qu_test) < Good[0]:
					Good = [abs(L/Qu_test), a/10, b/10, k/10, e/10]
					print("Good:", Good)
				
print(test)
