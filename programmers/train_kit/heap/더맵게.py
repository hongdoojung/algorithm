import heapq

def solution(scoville, K):
    heap = []
    for food in scoville:
        heapq.heappush(heap, food)
    answer = 0
    while heap[0] < K and len(heap) > 1:
        heapq.heappush(heap, heapq.heappop(heap) + 2 * heapq.heappop(heap))
        answer += 1
    if heap[0] < K:
        return -1
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([1, 2], 7))
    print(solution([1, 2, 3, 9, 10, 12, 1, 2, 3, 9, 10, 12, 1, 2, 3, 9, 10, 12, 1, 2, 3, 9, 10, 12], 7))
    print(solution([1, 2, 3, 9, 10, 12], 7777))