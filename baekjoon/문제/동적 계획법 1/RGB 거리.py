def min_cost(houses, costs):
    index = len(costs)
    cost = []
    last_min = costs[index-1].index(min(costs[index-1]))
    cost.append(min(costs[index-1]) + houses[index][0])
    cost.append(min(costs[index-1]) + houses[index][1])
    cost.append(min(costs[index-1]) + houses[index][2])
    cost[last_min] = sorted(costs[index-1])[1] + houses[index][last_min]
    costs.append(cost)
    return costs

how_many = int(input())
houses = []
for row in range(how_many):
    cost = list(map(int, input().split()))
    houses.append(cost)

costs = [houses[0]]
for index in range(how_many - 1):
    costs = min_cost(houses, costs)
print(min(costs[-1]))
