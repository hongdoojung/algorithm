import sys


def main():
    N = int(sys.stdin.readline())
    how_many_lines = int(sys.stdin.readline())
    lines = [[] for i in range(N+1)]
    computers = [0] * (N+1)
    # print(lines)
    # print(computers)
    for i in range(how_many_lines):
        a, b = (map(int, sys.stdin.readline().split()))
        lines[a].append(b)
        lines[b].append(a)

    candidates = [1]
    computers[1] = 1
    answer = 0
    while candidates:
        new_candidates = []
        for candidate in candidates:
            for computer in lines[candidate]:
                if computers[computer] == 0:
                    computers[computer] = 1
                    answer += 1
                    new_candidates.append(computer)
        # print(1111, candidates, new_candidates, candidate)
        # print(2222, computers, lines, answer)
        candidates = new_candidates
    print(answer)



if __name__ == "__main__":
    main()
