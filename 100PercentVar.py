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


hide_p = []
len_road = 0
for g in range(n):
    max_v = 0
    for i in range(n):
        for j in range(n):
            con = 0
            for k in range(len(hide_p)):
                if hide_p[k][0] == i or hide_p[k][1] == j:
                    con = 1
            if i == j or con == 1 or matrix_s[i][j] == -1:
                continue

            if max_v <= matrix_s[i][j]:
                hide_p.append([i, j])
                max_v = matrix_is[i][j]

    len_road += max_v


print(len_road)

