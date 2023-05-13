def main():
    length, part_length = (map(int, input().split()))
    array = list(map(int, input().split()))

    part_sum = sum(array[0:part_length])
    max_part_sum = part_sum
    for i in range(length - part_length):
        part_sum = part_sum - array[i] + array[i + part_length]
        max_part_sum = max(max_part_sum, part_sum)
    print(max_part_sum)


if __name__ == "__main__":
    main()
