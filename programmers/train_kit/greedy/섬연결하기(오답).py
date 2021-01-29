# 모든 섬을 연결하는 최소비용을 산출해야하는 문제인데,
# 문제를 잘못 이해하여 한 섬에서 모든 섬으로 가는 최소비용을 구함 

def solution(n, costs):
    counter = []
    biggest = []
    for a in range(len(costs)):
        biggest.append(max(costs[a]))
    biggest = max(biggest)*n        
    for a in range(n):
        counter.append([])
        for b in range(n):
            counter[a].append(biggest)
            if a == b:
                counter[a][a] = 0
    for cost in costs:
        counter[cost[0]][cost[1]] = cost[2]
        counter[cost[1]][cost[0]] = cost[2]

    min_costs = counter[0]
    if len(min_costs) == 1:
        return 0

    answer = 0
    connects = [0]
    while len(connects) != n:
        sorted_min_costs = sorted(min_costs)
        next_connect = min_costs.index(sorted_min_costs[len(connects)])
        k = 1

        while next_connect in connects:
            next_connect = min_costs.index(sorted_min_costs[len(connects)]) + k
            k += 1

        for a in range(n):
            if min_costs[a] > counter[next_connect][a] + min_costs[next_connect]:
                min_costs[a] = counter[next_connect][a] + min_costs[next_connect]
        connects.append(next_connect)
    return min_costs

if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
