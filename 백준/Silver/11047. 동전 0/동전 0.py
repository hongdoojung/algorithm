def main():
    how_many, target = (map(int, input().split()))
    coin_types = []
    for i in range(how_many):
        coin_types.append(int(input()))

    sum = 0
    coin_types.reverse()
    for coin_type in coin_types:
        sum += int(target / coin_type)
        target %= coin_type
    print(sum)

    
if __name__ == "__main__":
    main()
