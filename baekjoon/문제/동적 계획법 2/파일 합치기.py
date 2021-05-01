def collect_inputs():
    how_many = int(input())
    lines = []
    for i in range(how_many):
        input()
        line = list(map(int, input().split()))
        lines.append(line)
    return lines

def calculate_min_sum(line):
    length = len(line)
    costs = [line[0]]
    for i in range(1, len(line)):
        costs.append(costs[i-1] + line[i])

    dp = [[0]*(length) for _ in range(length)]
    for i in range(length - 1):
        dp[i][i+1] = line[i] + line[i+1]

    for j in range(2, length):
        i = 0
        while i + j < length:
            for k in range(i, i+j):
                cost_dist = costs[i+j] - costs[i-1] if i!=0 else costs[i + j]
                if dp[i][i+j] == 0:
                    dp[i][i+j] = dp[i][k] + dp[k+1][i+j] + cost_dist
                else:
                    dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+j] + cost_dist)
            i += 1
    return dp[0][-1]
    
if __name__ == "__main__":
    lines = collect_inputs()
    for line in lines:
        print(calculate_min_sum(line))
