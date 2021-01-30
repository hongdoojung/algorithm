# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

# 제한사항

# 섬의 개수 n은 1 이상 100 이하입니다.
# costs의 길이는 ((n-1) * n) / 2이하입니다.
# 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
# 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
# 연결할 수 없는 섬은 주어지지 않습니다.
# 입출력 예

# n	costs	return
# 4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
# 입출력 예 설명

# costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.

def find_disconnectable(island0, island1, matrix):
    matrix[island0][island1] = 0
    matrix[island1][island0] = 0
    
    connected = [island0]
    attempt = 0
    while attempt < len(matrix):
        next_connected = connected
        for connect in connected:
            for i in range(len(matrix)):
                if matrix[connect][i] and i not in next_connected:
                    if i == island1:
                        return True
                    next_connected.append(i)
        attempt += 1
        connected = next_connected

    matrix[island0][island1] = 1
    matrix[island1][island0] = 1
    return False

def solution(n, costs):
    matrix = []
    for a in range(n):
        matrix.append([])
        for b in range(n):
            matrix[a].append(0)
            if a == b:
                matrix[a][a] = 0
    for cost in costs:
        matrix[cost[0]][cost[1]] = 1
        matrix[cost[1]][cost[0]] = 1

    answer = 0
    while costs:
        costs.sort(key=lambda x: x[2])
        disconnect = find_disconnectable(costs[-1][0], costs[-1][1], matrix)
        if disconnect:
            pass
        else:
            answer += costs[-1][2]
        costs.pop()
    return answer
