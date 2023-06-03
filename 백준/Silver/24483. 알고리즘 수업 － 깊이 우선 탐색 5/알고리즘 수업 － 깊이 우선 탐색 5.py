import sys
import heapq

sys.setrecursionlimit(10**6)


def dfs(R, E, V, DV, indexs, depth):
    # print("called", R, V, indexs)
    V[R] = indexs.pop(0)
    DV[R] = depth
    depth += 1
    heap = []
    for v in E[R]:
        if not V.get(v):
            heapq.heappush(heap, v)
    while heap:
        min_value = heapq.heappop(heap)
        if not V.get(min_value):
            dfs(min_value, E, V, DV, indexs, depth)


# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

def main():
    N, M, R = list(map(int, sys.stdin.readline().split()))

    E = [[] for _ in range(N+1)]
    V = dict()
    DV = dict()
    for i in range(M):
        a, b = list(map(int, sys.stdin.readline().split()))
        E[a].append(b)
        E[b].append(a)

    indexs = [i for i in range(1, N + 1)]
    depth = 0
    dfs(R, E, V, DV, indexs, depth)
    
    result = 0
    # print(V)
    # print(DV)
    for i in range(1, N + 1):
        result += (V.get(i, 0) * DV.get(i, -1))
    print(result)

if __name__ == "__main__":
    main()
