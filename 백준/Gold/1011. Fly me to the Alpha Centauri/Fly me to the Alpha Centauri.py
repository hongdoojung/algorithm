def main():
    length = int(input())
    distances = []
    for i in range(length):
        start, end = (map(int, input().split()))
        distances.append(end - start)
    for distance in distances:
        current = 1
        while current ** 2 <= distance:
            current += 1
            5, 21
        candidate = current - 1
        if candidate ** 2 == distance:
            print(candidate * 2 - 1)
        elif candidate ** 2 + candidate >= distance:
            print(candidate * 2)
        else:
            print(candidate * 2 + 1)

    
if __name__ == "__main__":
    main()
