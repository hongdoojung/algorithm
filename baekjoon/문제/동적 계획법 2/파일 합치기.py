# 이해못함
how_many = int(input())
lines = []
for i in range(how_many):
    input()
    line = list(map(int, input().split()))
    lines.append(line)

for line in lines: 
    sum = [line[0]]
    for i in line[1:]: 
        sum.append(i + sum[-1]) 
    accumulated = [[0] * len(line) for _ in range(len(line))]
    
    accumulated[0][1] = sum[1] 
    for i in range(1, len(line) - 1):
        accumulated[i][i + 1] = sum[i + 1] - sum[i - 1] 
    for gap in range(2, len(line)): 
        for i in range(len(line) - gap): 
            accumulated[i][i + gap] = float('inf') 
            for j in range(i, i + gap): 
                accumulated[i][i + gap] = min(accumulated[i][i + gap], accumulated[i][j] + accumulated[j + 1][i + gap]) 
            accumulated[i][i + gap] = accumulated[i][i + gap] + sum[i + gap] - sum[i - 1] if i > 0 else accumulated[0][gap] + sum[gap]
    print(accumulated[0][len(line) - 1])
