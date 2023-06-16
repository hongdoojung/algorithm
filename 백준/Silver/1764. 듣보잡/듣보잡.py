import sys


def main():
    X, Y = (map(int, sys.stdin.readline().split()))
    xs = []
    for i in range(X):
        xs.append(sys.stdin.readline().rstrip("\n"))
    
    ys = []
    for i in range(Y):
        ys.append(sys.stdin.readline().rstrip("\n"))
        
    xs.sort()
    ys.sort()
    
    answer = []
    i = 0
    j = 0
    while j < len(ys) and i < len(xs):
        if xs[i] < ys[j]:
            i += 1
        elif xs[i] > ys[j]:
            j += 1
        else:
            answer.append(xs[i])
            i += 1
            j += 1
    
    print(len(answer))
    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
