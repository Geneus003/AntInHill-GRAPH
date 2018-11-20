import graph
import perebor
import time


def main_func(Qu):
  rezult = {}
  
  for i in range(Qu):
    print(i)
    matrix, n = graph.generate_graph()
    time_ = time.time()
    len_, road = perebor.mainus(matrix, n)
    time_ = time.time() - time_
    rezult = [matrix, n, len_, time_]
    f = open('graph_with_len.txt', 'ta', encoding="utf-8")
    print(rezult[1], rezult[2], rezult[3], file=f)
    for j in range(rezult[1]):
      for l in range(rezult[1]):
        print(rezult[0][j][l], end=" ", file=f)
      print(file=f)

    print(file=f)
    f.close()
  return rezult


if __name__ == "__main__":
  main_func(500)
