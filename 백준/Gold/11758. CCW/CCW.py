import sys


def main():
    p1x, p1y = (map(int, sys.stdin.readline().split()))
    p2x, p2y = (map(int, sys.stdin.readline().split()))
    p3x, p3y = (map(int, sys.stdin.readline().split()))
    
    if p2x == p1x:
        if p2y > p1y:
            if p3x > p1x:
                print(-1)
            elif p3x < p1x:
                print(1)
            else:
                print(0)
        elif p2y < p1y:
            if p3x > p1x:
                print(1)
            elif p3x < p1x:
                print(-1)
            else:
                print(0)
        else:
            print(0)
        return
    slope = (p2y - p1y) / (p2x - p1x)
    if (p2y - p1y) / (p2x - p1x) == (p3y - p1y) / (p3x - p1x) or (p2y - p1y) / (p2x - p1x) == (p3y - p2y) / (p3x - p2x):
        print(0)
        return
    if p2x > p1x:
        if slope * (p3x - p1x) + p1y > p3y:
            print(-1)
        elif slope * (p3x - p1x) + p1y < p3y:
            print(1)
        else:
            print(0)
    elif p2x < p1x:
        if slope * (p3x - p1x) + p1y > p3y:
            print(1)
        elif slope * (p3x - p1x) + p1y < p3y:
            print(-1)
        else:
            print(0)


if __name__ == "__main__":
    main()
