import random


def generate_graph():

    n = random.randint(4, 6)    # n - количество вершин графа

    matrix_graph = []  # matrix_graph - матрица соеденений графа

    #  Генерация графа и заполнение нолями
    for i in range(n):
        matrix_graph.append([])
        for j in range(n):
            matrix_graph[i].append(-1)

    # Генерация случайного числа которое будет самым большим в графе и 2 самых маленьких
    huge_var = random.randint(20, 40)
    first_min_var = int(huge_var/2)
    second_min_var = first_min_var + 1

    def generate_grafik():
        # Функция генерирующая отрезки
        for i in range(n):
            for j in range(n):
                if j <= i:
                    continue
                temp_var = random.randint(second_min_var, huge_var)
                matrix_graph[i][j] = temp_var
                matrix_graph[j][i] = temp_var

    generate_grafik()

    # Изменение параметров (1,1) (2,2) и т.д на 1000
    for i in range(n):
        for j in range(n):
            if i != j:
                continue
            else:
                matrix_graph[i][j] = -2

    return matrix_graph, n


"""
P.S Проверка графа - это если два минимальных числа в сумме дают больше, чем  самое большое, то граф выполняется
P.S.S Можно найти большую сторону создать два числа которые дают на 1 больше (10) и (5,6) все остальные расстояния
генерировать в диапозоне от (6,10) -> они уже будут больше
"""