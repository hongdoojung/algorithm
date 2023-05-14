import heapq
import sys

def main():
    length = int(input())
    array = []
    for i in range(length):
        heapq.heappush(array, int(sys.stdin.readline()))
    
    num = 0
    for i in range(length-1):
        left = heapq.heappop(array)
        right = heapq.heappop(array)
        current = left + right
        num += current
        heapq.heappush(array, current)
    print(num)

if __name__ == "__main__":
    main()
