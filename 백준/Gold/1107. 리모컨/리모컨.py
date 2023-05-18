def main():
    target = int(input())
    broken = int(input())
    candidate = abs(100 - target)
    if broken == 0:
        brokens = set()
    else:
        brokens = set(map(int, input().split()))

    for i in range(1000001): 
        for stri in str(i):
            if int(stri) in brokens:
                break
        else:
            candidate = min([len(str(i)) + abs(i - target), candidate])

    print(candidate)
    
if __name__ == "__main__":
    main()
