import sys


def main():
    N, M, H = map(int, (sys.stdin.readline().split()))
    
    ones = []
    floors = []
    for k in range(H):
        rows = []
        for i in range(M):
            rows.append(list(map(int, (sys.stdin.readline().split()))))
            for j in range(N):
                if rows[-1][j] == 1:
                    ones.append((k, i, j))
        floors.append(rows)

    answer = 0
    while ones:
        new_ones = []
        for onek, onei, onej in ones:
            if onei > 0 and floors[onek][onei - 1][onej] == 0:
                floors[onek][onei - 1][onej] = 1
                new_ones.append((onek,onei - 1,onej))
            if onei < M - 1 and floors[onek][onei + 1][onej] == 0:
                floors[onek][onei + 1][onej] = 1
                new_ones.append((onek,onei + 1,onej))
            if onej > 0 and floors[onek][onei][onej - 1] == 0:
                floors[onek][onei][onej - 1] = 1
                new_ones.append((onek,onei,onej - 1))
            if onej < N - 1 and floors[onek][onei][onej + 1] == 0:
                floors[onek][onei][onej + 1] = 1
                new_ones.append((onek,onei,onej + 1))
            if onek > 0 and floors[onek - 1][onei][onej] == 0:
                floors[onek - 1][onei][onej] = 1
                new_ones.append((onek - 1,onei,onej))
            if onek < H - 1 and floors[onek + 1][onei][onej] == 0:
                floors[onek + 1][onei][onej] = 1
                new_ones.append((onek + 1,onei,onej))
        # print(rows)
        # print(ones)
        ones = new_ones
        if ones:
            answer += 1

    for rows in floors:
        for row in rows:
            if 0 in row:
                print(-1)
                return
    print(answer)


if __name__ == "__main__":
    main()
