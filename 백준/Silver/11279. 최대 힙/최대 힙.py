import sys
import heapq

how_many = int(input())
cases = []
for i in range(how_many):
    cases.append(int(sys.stdin.readline()))

heap = []
for case in cases:
    if case == 0:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -1 * case)
