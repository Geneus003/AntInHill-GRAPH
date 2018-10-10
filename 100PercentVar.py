import graph
import copy

matrix, n = graph.generate_graph()  # Подключение графа

matrix_is = copy.deepcopy(matrix)

print()

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

stl_mas_min = []    # Массив с минисальным значением в столбце

for i in range(n):      # Нахождения мимума в столбце
    min_zn = 1000
    for j in range(n):
        if min_zn > matrix[j][i]:
            min_zn = matrix[j][i]

    stl_mas_min.append(min_zn)


for i in range(n):      # Редукция по столбам(отнимаем минимум)
    for j in range(n):
        matrix[j][i] -= stl_mas_min[i]

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
                if matrix[i][h] < min_str:
                    min_str = matrix[i][h]
            for g in range(n):
                if g == i:
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

for i in range(n):
    print()
    for j in range(n):
        print(matrix_s[i][j]," ", end="")

print()

len_road = 0
off_klet = []
us_town = []

for k in range(n):
    if len(us_town) == n:
        break
    max_v = 0
    ch_klet = [0, 0]
    ch_past = -1
    for i in range(n):
        for j in range(n):
            con = 0
            for k in range(len(off_klet)):
                if off_klet[k] == [i, -1] or off_klet[k] == [-1, j]:
                    con = 1
            if max_v < matrix_s[i][j] and con == 0:
                max_v = matrix_s[i][j]
                ch_klet = [i, j]

    off_klet.append([ch_klet[0], -1])
    off_klet.append([-1, ch_klet[1]])
    print(ch_klet[0], ch_klet[1])

    if k == 0:
        us_town.append(ch_klet[0])
        us_town.append(ch_klet[1])
    else:
        q = 0
        for l in range(len(us_town)):
            if us_town[l] == ch_klet[0]:
                q = 1
        if q == 0:
            us_town.append(ch_klet[0])

        q = 0
        for l in range(len(us_town)):
            if us_town[l] == ch_klet[1]:
                q = 1
        if q == 0:
            us_town.append(ch_klet[1])

for i in range(n):
    print()
    for j in range(n):
        print(matrix_is[i][j]," ", end="")

for i in range(len(us_town) - 1):
    len_road += matrix_is[us_town[i]][us_town[i + 1]]

len_road += matrix_is[us_town[len(us_town) - 1]][us_town[0]]

print(len_road)