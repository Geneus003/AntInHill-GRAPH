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


def main_func(matrix, matrix_is, n, le_road, matrix_us_town):
    for q in range(n):

        s = 0
        for i in range(n):
            for j in range(n):
                s += matrix[i][j]

        if s == (-2 * n):
            break

        def red_str(matrix, n):
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

            return matrix

        matrix = copy.deepcopy(red_str(matrix, n))

        def red_stl(matrix, n):
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

            return matrix

        matrix = copy.deepcopy(red_stl(matrix, n))

        def red_tab(matrix, n):
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

            return matrix, matrix_s

        ot = red_tab(matrix, n)

        matrix, matrix_s = copy.deepcopy(ot[0]), copy.deepcopy(ot[1])

        def find_max_cof(matrix_s):
            max_cof = -3
            max_cof_kor = []
            max_cof_kor.append([])
            max_cof_kor[0] = [-1, -1]

            for i in range(n):
                for j in range(n):
                    if matrix_s[i][j] == -1:
                        continue
                    else:
                        if matrix_s[i][j] >= max_cof:
                            max_cof = matrix_s[i][j]
                            max_cof_kor[0] = [i, j]

            for i in range(n):
                for j in range(n):
                    if matrix_s[i][j] == -1:
                        continue
                    if i == max_cof_kor[0][0] and j == max_cof_kor[0][1]:
                        continue

                    if matrix[i][j] == max_cof:
                        max_cof_kor.append([i, j])

            return max_cof_kor

        max_cof_kor = find_max_cof(matrix_s)

        if len(matrix_us_town) == 0:
            matrix_us_town.append(max_cof_kor[0][0])
            matrix_us_town.append(max_cof_kor[0][1])
        else:
            if max_cof_kor[0][0] in matrix_us_town:
                y = 0
            else:
                matrix_us_town.append(max_cof_kor[0][0])
            if max_cof_kor[0][1] in matrix_us_town:
                y = 0
            else:
                matrix_us_town.append(max_cof_kor[0][1])

        le_road += matrix_is[max_cof_kor[0][0]][max_cof_kor[0][1]]

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -2:
                    continue
                if i == max_cof_kor[0][0]:
                    matrix[i][j] = -2
                if j == max_cof_kor[0][1]:
                    matrix[i][j] = -2

        matrix[max_cof_kor[0][1]][max_cof_kor[0][0]] = -2

        max_cof_kor = []

    return matrix, le_road


matrix, le_road = main_func(matrix, matrix_is, n, le_road, matrix_us_town)

print(le_road)
