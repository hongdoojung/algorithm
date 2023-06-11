import sys


def main():
    N, M = (map(int, sys.stdin.readline().split()))
    rows = []
    answers = []
    for i in range(N):
        answers.append([-1]*M)
    for i in range(N):
        rows.append(list(map(int, sys.stdin.readline().split())))
        for j in range(M):
            if rows[-1][j] == 2:
                start = (i,j)
            if rows[-1][j] == 0:
                answers[i][j] = 0
    # print(rows)
    # print(answers)
    candidates = [start]
    
    answers[start[0]][start[1]] = 0
    k = 1
    while candidates:
        new_candidates = []
        for i, j in candidates:
            if i > 0 and rows[i-1][j] == 1 and answers[i-1][j] == -1:
                answers[i-1][j] = k
                new_candidates.append((i-1, j))
            if i < N-1 and rows[i+1][j] == 1 and answers[i+1][j] == -1:
                answers[i+1][j] = k
                new_candidates.append((i+1, j))
            if j > 0 and rows[i][j-1] == 1 and answers[i][j-1] == -1:
                answers[i][j-1] = k
                new_candidates.append((i, j-1))
            if j < M-1 and rows[i][j+1] == 1 and answers[i][j+1] == -1:
                answers[i][j+1] = k
                new_candidates.append((i, j+1))
        k += 1
        candidates = new_candidates
        # print(candidates)

    for i in range(N):
        stranswer = ' '.join(map(str,answers[i]))
        print(stranswer)


if __name__ == "__main__":
    main()
