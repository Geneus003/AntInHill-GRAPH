def StartProc():

    import graph
    import copy

    matrix, n = graph.generate_graph()  # Подключение графа

    """
    
    matrix = [[-2, 20, 18, 12, 8], [5, -2, 14, 7, 11], [12, 18, -2, 6, 11], [11, 17, 11, -2, 12], [5, 5, 5, 5, -2]]
    
    n = 5
    """
    matrix_is = copy.deepcopy(matrix)
    le_road = 0


    def main_func(matrix, matrix_is, n, le_road):

        s = 0
        for i in range(n):
            for j in range(n):
                s += matrix[i][j]

        if s == (-2 * n * n):
            return le_road, matrix

        def red_str(matrix, n):
            str_mas_min = []  # Массив с минимальными значениями в строке

            for i in range(n):  # Нахождение минимального числа
                min_zn = 1000
                for j in range(n):
                    if matrix[i][j] == -2:
                        continue
                    if matrix[i][j] < min_zn:
                        min_zn = matrix[i][j]

                str_mas_min.append(min_zn)

            for i in range(n):  # Отнимаем минимальное число из строки
                for j in range(n):
                    if matrix[i][j] == -2:
                        continue
                    matrix[i][j] -= str_mas_min[i]

            return matrix

        matrix = copy.deepcopy(red_str(matrix, n))

        def red_stl(matrix, n):
            stl_mas_min = []  # Массив с минисальным значением в столбце

            for i in range(n):  # Нахождения мимума в столбце
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
            matrix_s = []  # Таблица с коэфицентами для ноля
            for i in range(n):  # Вычиселния коэфицента
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

        min_road = 10000

        for q in range(len(max_cof_kor)):

            now_road = le_road
            matrix_w = copy.deepcopy(matrix)

            now_road += matrix_is[max_cof_kor[q][0]][max_cof_kor[q][1]]

            for i in range(n):
                for j in range(n):
                    if matrix_w[i][j] == -2:
                        continue
                    if i == max_cof_kor[q][0]:
                        matrix_w[i][j] = -2
                    if j == max_cof_kor[q][1]:
                        matrix_w[i][j] = -2

            matrix_w[max_cof_kor[q][1]][max_cof_kor[q][0]] = -2

            le, matrix_w = main_func(matrix_w, matrix_is, n, now_road)

            if le <= min_road:
                min_road = le

        s = 0
        for i in range(n):
            for j in range(n):
                s += matrix_w[i][j]

        if s == (-2 * n * n):
            return le, matrix_w

        return le_road, matrix

    le_road, matrix = main_func(matrix, matrix_is, n, le_road)

    return le_road, matrix_is, n


le, m = StartProc()
