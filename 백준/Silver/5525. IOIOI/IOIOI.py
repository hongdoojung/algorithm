import sys

def main():
    N = int(sys.stdin.readline())
    S_length = int(sys.stdin.readline())
    S = sys.stdin.readline()

    PN = ("IO" * (N + 1))[:-1]
    answer = 0
    for i in range(len(S) - len(PN)):
        if S[i:i + len(PN)] == PN:
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
