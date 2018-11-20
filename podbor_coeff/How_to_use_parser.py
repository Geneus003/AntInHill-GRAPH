import Parsing_f

con = 0
pr = 0
for i in range(500):
	a, b, c, matrix = Parsing_f.parser(con + pr)

	# body of code THIS CONSTRUCTION IS REQUERED !!! ЭТА КОНСТРУКЦИЯ НУЖНА ПРОСТО ДОПИШИ ТЕЛО

	print(a, b, c, matrix)

	pr += a + 2
