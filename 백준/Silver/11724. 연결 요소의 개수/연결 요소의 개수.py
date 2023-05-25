import sys

def main():
    N, how_many = map(int, (sys.stdin.readline().split()))
    inputs = []
    graphs = []
    input_nums = set()
    for i in range(how_many):
        a, b = sys.stdin.readline().split()
        inputs.append([a, b])
        input_nums.add(a)
        input_nums.add(b)

    for a, b in inputs:
        find = -1
        for i, graph in enumerate(graphs):
            # print(99999, graphs, a, b, i, find)
            if find != -1 and (a in graph or b in graph):
                # print(111111,i, find)
                graphs.append(graphs[i].union(graphs[find]))
                del graphs[i]
                del graphs[find]
                break
            elif a in graph or b in graph:
                # print(222222,i, find)
                find = i
                graph.add(a)
                graph.add(b)
                continue
        if find == -1:
            # print(33333, graphs,a, b)
            graphs.append(set([a, b]))

    # print(graphs)
    left = N - len(input_nums)
    print(len(graphs) + left)


if __name__ == "__main__":
    main()
