def main():
    bottles, capacity = (map(int, input().split()))
    remain = bottles
    last_biggest = 1
    while remain > 0 and capacity > 0:
        biggest = 1
        while biggest <= remain:
            biggest = biggest * 2
        biggest /= 2
        last_biggest = biggest
        if remain - biggest > 0:
            remain -= biggest 
            capacity -= 1
        else:
            break
    print(int(last_biggest - remain))

if __name__ == "__main__":
    main()
