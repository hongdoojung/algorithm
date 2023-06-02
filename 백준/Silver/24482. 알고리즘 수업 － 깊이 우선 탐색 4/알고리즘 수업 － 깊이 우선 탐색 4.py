import sys
import heapq

sys.setrecursionlimit(10**6)


def dfs(R, E, V, depth):
    # print("called", R, V, indexs)
    V[R] = depth
    depth += 1
    heap = []
    for v in E[R]:
        if not V.get(v):
            heapq.heappush(heap, -1*v)
    while heap:
        min_value = -1*heapq.heappop(heap)
        if not V.get(min_value):
            dfs(min_value, E, V, depth)


# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

def main():
    N, M, R = list(map(int, sys.stdin.readline().split()))

    E = [[] for _ in range(N+1)]
    V = dict()
    for i in range(M):
        a, b = list(map(int, sys.stdin.readline().split()))
        E[a].append(b)
        E[b].append(a)

    depth = 1
    dfs(R, E, V, 1)
    for i in range(1, N + 1):
        print(V.get(i, 0) - 1)


if __name__ == "__main__":
    main()

# 6 7 1
# 1 6
# 1 2
# 2 6
# 2 3
# 2 4
# 3 5
# 4 5