import graph
import copy

matrix, n = graph.generate_graph()  # Подключение графа

matrix_is = copy.deepcopy(matrix)

for i in range(n):
    print()
    for j in range(n):
        print(matrix_is[i][j], " ", end="")
print()
matrix_us_town = []
le_road = 0

for q in range(n):

    str_mas_min = []    # Массив с минимальными значениями в строке

    for i in range(n):      # Нахождение минимального числа
        min_zn = 1000
        for j in range(n):
            if matrix[i][j] == -2:
                continue
            if matrix[i][j] < min_zn:
                min_zn = matrix[i][j]

        str_mas_min.append(min_zn)

    for i in range(n):      # Отнимаем минимальное число из строки
        for j in range(n):
            if matrix[i][j] == -2:
                continue
            matrix[i][j] -= str_mas_min[i]

    for i in range(n):
        print()
        for j in range(n):
            print(matrix[i][j]," ", end="")

    print()

    stl_mas_min = []    # Массив с минисальным значением в столбце

    for i in range(n):      # Нахождения мимума в столбце
        min_zn = 1000
        for j in range(n):
            if matrix[j][i] == -2:
                continue
            if min_zn > matrix[j][i]:
                min_zn = matrix[j][i]

        stl_mas_min.append(min_zn)

    for i in range(n):  # Редукция по столбам(отнимаем минимум)
        for j in range(n):
            if matrix[j][i] == -2:
                continue
            matrix[j][i] -= stl_mas_min[i]

    for i in range(n):
        print()
        for j in range(n):
            print(matrix[i][j]," ", end="")

    print()

    matrix_s = []   # Таблица с коэфицентами для ноля
    for i in range(n):      # Вычиселния коэфицента
        matrix_s.append([])
        for j in range(n):

            if matrix[i][j] == 0:
                min_str = 10000
                min_stl = 10000
                for h in range(n):
                    if h == j:
                        continue
                    if matrix[i][h] == -2:
                        continue
                    if matrix[i][h] < min_str:
                        min_str = matrix[i][h]
                for g in range(n):
                    if g == i:
                        continue
                    if matrix[g][j] == -2:
                        continue
                    if matrix[g][j] < min_stl:
                        min_stl = matrix[g][j]

                matrix_s[i].append(min_stl + min_str)
            else:
                matrix_s[i].append(-1)


    for i in range(n):
        print()
        for j in range(n):
            print(matrix[i][j]," ", end="")

    print()

    for i in range(n):
        print()
        for j in range(n):

            print(matrix_s[i][j]," ", end="")

    print()

    max_cof = -3
    max_cof_kor = [-1, -1]

    for i in range(n):
        for j in range(n):
            if matrix_s[i][j] == -1:
                continue
            else:
                if matrix_s[i][j] >= max_cof:
                    max_cof = matrix_s[i][j]
                    max_cof_kor = [i, j]

    if len(matrix_us_town) == 0:
        matrix_us_town.append(max_cof_kor[0])
        matrix_us_town.append(max_cof_kor[1])
    else:
        if max_cof_kor[0] in matrix_us_town:
            y = 0
        else:
            matrix_us_town.append(max_cof_kor[0])
        if max_cof_kor[1] in matrix_us_town:
            y = 0
        else:
            matrix_us_town.append(max_cof_kor[1])

    le_road += matrix_is[max_cof_kor[0]][max_cof_kor[1]]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -2:
                continue
            if i == max_cof_kor[0]:
                matrix[i][j] = -2
            if j == max_cof_kor[1]:
                matrix[i][j] = -2

    matrix[max_cof_kor[1]][max_cof_kor[0]] = -2

    for i in range(n):
        print()
        for j in range(n):
            print(matrix[i][j]," ", end="")

    print()

    print(max_cof_kor, matrix_us_town)

    print()
    print()


print(le_road)