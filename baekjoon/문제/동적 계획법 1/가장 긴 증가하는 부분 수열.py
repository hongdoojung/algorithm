how_many = int(input())
numbers = list(map(int, input().split()))
longest_subsequence = []

for index in range(how_many):
    if index == 0:
        longest_subsequence.append(1)
    else:
        max_sub_longest = 0
        for index_2 in range(index):
            if numbers[index_2] < numbers[index] and longest_subsequence[index_2] > max_sub_longest:
                max_sub_longest = longest_subsequence[index_2]
        longest_subsequence.append(max_sub_longest + 1)

print(max(longest_subsequence))