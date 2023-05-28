import sys
import heapq


def bfs(E, V, Q):
    i = 1
    checked = 0
    next_us = [*Q]
    while len(E) != checked and next_us:
        us = [*next_us]
        next_us = []
        # print(len(E), us, checked)
        while us:
            u = us.pop(0)
            heap = []
            for v in E[u]:
                if not V.get(v):
                    heapq.heappush(heap, v)
                    checked += 1
            # print(Q, u, heap)
            while heap:
                point = heapq.heappop(heap)
                next_us.append(point)
                V[point] = i
        i += 1


def main():
    N, M, R = list(map(int, sys.stdin.readline().split()))

    E = [[] for _ in range(N+1)]
    V = dict()
    for i in range(M):
        a, b = list(map(int, sys.stdin.readline().split()))
        E[a].append(b)
        E[b].append(a)

    Q = []
    Q.append(R)
    V.update({R: 1})

    bfs(E, V, Q)
    V.update({R: 0})
    for i in range(1, N + 1):
        print(V.get(i, -1))


if __name__ == "__main__":
    main()


# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }
