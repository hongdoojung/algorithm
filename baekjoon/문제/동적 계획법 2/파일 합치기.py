# 이해못함
how_many = int(input())
lines = []
for i in range(how_many):
    input()
    line = list(map(int, input().split()))
    lines.append(line)

for line in lines:
    dp = list(list(0 for _ in range(len(line))) for _ in range(len(line)))
    for k in range(1,len(line)):
        for i in range(len(line)-k):
            x, y = i, i+k
            for j in range(k):
                tmp = dp[x + 1 + j][y]+dp[x][y - k + j]
                dp[x][y] = min(dp[x][y],tmp) if dp[x][y]>0 else tmp
            dp[x][y] += sum(line[x : y + 1])
    print(dp[0][-1])
