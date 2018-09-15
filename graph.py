import random


def generate_graph():

    n = random.randint(4, 20)  # n - количество вершин графа

    matrix_graph = []  # matrix_graph - матрица соеденений графа

    #  Генерация графа и заполнение нолями
    for i in range(n):
        matrix_graph.append([])
        for j in range(n):
            matrix_graph[i].append(-1)

    # Генерация случайного графа
    for i in range(n):
        for j in range(n):
            temp_v = random.randint(3, 20)
            matrix_graph[i][j] = temp_v
            matrix_graph[j][i] = temp_v

    # Функция исправления графа(перебор разных чисел до правила треугольника)
    def fix_graph():
        for i in range(n):
            for j in range(n):
                for g in range(n):

                    if matrix_graph[i][j] + matrix_graph[j][g] <= matrix_graph[g][i]:
                        temp_v = matrix_graph[g][i] - matrix_graph[j][g]
                        temp_vv = random.randint(temp_v + 1, temp_v + 10)
                        matrix_graph[i][j] = temp_vv
                        matrix_graph[j][i] = temp_vv
                        return 0

                    elif matrix_graph[j][g] + matrix_graph[g][i] <= matrix_graph[i][j]:
                        temp_v = matrix_graph[i][j] - matrix_graph[g][i]
                        temp_vv = random.randint(temp_v + 1, temp_v + 10)
                        matrix_graph[j][g] = temp_vv
                        matrix_graph[g][j] = temp_vv
                        return 0

                    elif matrix_graph[g][i] + matrix_graph[i][j] <= matrix_graph[g][j]:
                        temp_v = matrix_graph[g][j] - matrix_graph[i][j]
                        temp_vv = random.randint(temp_v + 1, temp_v + 10)
                        matrix_graph[g][i] = temp_vv
                        matrix_graph[i][g] = temp_vv
                        return 0
        return 1

    # Исправление графа в виде постоянного перебора
    a = 0
    while a != 1:
        a = fix_graph()

    # Изменение параметров (1,1) (2,2) и т.д на 10000
    for i in range(n):
        for j in range(n):
            if i != j:
                continue
            else:
                matrix_graph[i][j] = 1000

    return matrix_graph, n


generate_graph()


"""
P.S Проверка графа - это если два минимальных числа в сумме дают больше, чем  самое большое, то граф выполняется
P.S.S Можно найти большую сторону создать два числа которые дают на 1 больше (10) и (5,6) все остальные расстояния
генерировать в диапозоне от (6,10) -> они уже будут больше
"""