def main():
    target, length = (map(int, input().split()))
    answer = []

    while length <= 100:
        avg = target / length
        x = avg - length/2 + 0.5
        if x % 1 == 0 and x * length + length * (length - 1)/2 == target and x >= 0:
            answer = [i + x for i in range(length)]
            break
        length += 1
    if answer:
        for i in answer:
            print(int(i), end= " ")
        print()
    else:
        print(-1)



if __name__ == "__main__":
    main()
