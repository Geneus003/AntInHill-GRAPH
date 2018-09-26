import graph

matrix, n = graph.generate_graph()  # Подключение графа

matrix_is = matrix

str_mas_min = []    # Массив с минимальными значениями в строке

for i in range(n):      # Нахождение минимального числа
    min_zn = 1000
    for j in range(n):
        if matrix[i][j] < min_zn:
            min_zn = matrix[i][j]

    str_mas_min.append(min_zn)

for i in range(n):      # Отнимаем минимальное число из строки
    for j in range(n):
        matrix[i][j] -= str_mas_min[i]

stl_mas_min = []    # Массив с инисальным значением в столбце

for i in range(n):      # Нахождения мимума в столбце
    min_zn = 1000
    for j in range(n):
        if min_zn > matrix[j][i]:
            min_zn = matrix[j][i]

    stl_mas_min.append(min_zn)


for i in range(n):      # Редукция по столбам(отнимаем минимум)
    for j in range(n):
        matrix[j][i] -= stl_mas_min[i]

matrix_h = matrix

for i in range(n):
    print()
    for j in range(n):
        print(matrix[i][j], " ", end="")

print()


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            min_str = 10000
            min_stl = 10000

            for g in range(n):
                if g == j:
                    continue
                if matrix[i][g] < min_str:
                    min_str = matrix[i][g]

            for g in range(n):
                if i == g:
                    continue
                if matrix[g][j] < min_stl:
                    min_stl = matrix[g][j]

            matrix_h[i][j] = min_str + min_stl

            print(min_stl, min_str)

        else:
            matrix_h[i][j] = 100

for i in range(n):
    print()
    for j in range(n):
        print(matrix_h[i][j], " ", end="")