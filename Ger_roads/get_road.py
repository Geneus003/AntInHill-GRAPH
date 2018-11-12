import graph, figny, MinRoadAlg, perebor
import copy


def main_func():
    while 1:
        def check_t(maska):
            st = maska[0][0]
            kon = maska[0][1]

            # print(st, kon)
            f = 0
            for i in range(len(maska)):
                if i == 0:
                    continue
                for j in range(len(maska)):
                    if kon == maska[j][0]:
                        kon = maska[j][1]
                        # print(kon)
                        break
                if kon == st and i < len(maska) - 1:
                    f = 1
                    break
            if f == 1:
                return False
                nt += 1
            else:
                return True

        matrix, n = graph.generate_graph()

        matrix_c = copy.deepcopy(matrix)

        """
        print(n)

        for j in range(n):
            for q in range(n):
                print(matrix[j][q], " ", end="")
            print()
            
        """

        le_road_alg, maska = MinRoadAlg.StartProc(matrix, n)

        for i in range(len(maska)):
            maska[i] = maska[i][0]

        if check_t(maska):
            break

    le_road_perebor, us_town = perebor.mainus(matrix_c, n)

    le_road_figny = figny.formicaio_main(matrix_c, n, [3.6, 3.8, 0.5, 1.0])

    print(n, le_road_perebor, le_road_alg, le_road_figny)


for i in range(100):
    main_func()