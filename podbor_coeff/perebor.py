import copy


def mainus(matrix, n):

    def main_func(road_lean, usless_towns, pred):

        road = road_lean

        if len(usless_towns) == n:
            road += matrix[pred][usless_towns[0]]
            #print(usless_towns, road)
            return road, usless_towns

        min_len_road = 10000
        some_t = []
        for j in range(n):
            if j in usless_towns:
                continue
            else:
                here_town = copy.deepcopy(usless_towns)
                here_town.append(j)
                len_road = road + matrix[pred][j]
                pr_t = j

                lenroad, uskatown = main_func(len_road, here_town, pr_t)

                if lenroad < min_len_road:
                    min_len_road = lenroad
                    some_t = copy.deepcopy(uskatown)

        return min_len_road, some_t

    def start_func():
        min_road = 1000000
        uska_t = []
        for i in range(1):

            le_road = 0
            us_town = []
            us_town.append(i)
            pr = i

            le_road, us_t = main_func(le_road, us_town, pr)

            if le_road < min_road:
                min_road = le_road
                uska_t = copy.deepcopy(us_t)

        return le_road, uska_t

    """
    if min_road > le_road_alg:
        print("True", min_road)
    else:
        print("False", min_road)
    """
    return start_func()
