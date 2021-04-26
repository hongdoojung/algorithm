#이해안됨
how_many = int(input())
lines = []
for i in range(how_many):
    input()
    line = list(map(int, input().split()))
    lines.append(line)

for line in lines:
    length = len(line)
    max_int = sum(line) * length
    dp = [[0]*(length+1) for i in range(length+1)]
    costs = [line[0]]

    for i in range(1, length):
        costs.append(costs[i-1]+line[i])
    costs.append(0)

    for gap in range(1, length):
        for start in range(length):
            end = start + gap
            if end == length:
                break
            dp[start][end] = max_int
            for i in range(start, end):
                candidate = dp[start][i] + dp[i+1][end] + (costs[end]-costs[start-1])
                dp[start][end] = min(dp[start][end], candidate)
    print(dp[0][length-1])
