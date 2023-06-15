import sys


N = int(sys.stdin.readline())
arrays = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arrays.append((a, b))
arrays.append((1000000001, 1000000001))
arrays = sorted(arrays)
lines = [arrays[0]]
i = 0
answer = 0

for a, b in arrays:
    if lines[i][1] < a:
        answer += lines[i][1] - lines[i][0]
        lines.append((a, b))
        i += 1
    else:
        lines[i] = (lines[i][0], max(lines[i][1], b))
print(answer)