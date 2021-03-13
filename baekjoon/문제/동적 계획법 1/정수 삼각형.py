def solution(triangle):
    cumulation = [triangle[0][0]]
    for y in range(1, len(triangle)):
        new_cumulation = []
        new_cumulation.append(cumulation[0]+triangle[y][0])
        for x in range(1, len(cumulation)):
            new_cumulation.append(max([cumulation[x-1]+triangle[y][x], cumulation[x]+triangle[y][x]]))
        new_cumulation.append(cumulation[-1]+triangle[y][-1])
        cumulation = new_cumulation
    return max(cumulation)

how_many = int(input())
lines = []
for i in range(how_many):
    line = list(map(int, input().split()))
    lines.append(line)

print(solution(lines))
