import sys

def main():
    N, r, c = map(int, sys.stdin.readline().split())

    n = N
    answer = 0
    while n != 0:
        if r > (2 ** (n-1)) - 1:
            down = 1
            r -=  (2 ** (n-1))
        else:
            down = 0
        if c > (2 ** (n-1)) - 1:
            right = 1
            c -=  (2 ** (n-1))
        else:
            right = 0
        answer +=  (2 ** (2 * (n-1))) * (right + down * 2)
        n -= 1
    print(answer)


if __name__ == "__main__":
    main()
