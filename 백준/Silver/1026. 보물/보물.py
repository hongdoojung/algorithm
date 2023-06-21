import sys

length = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)
B.sort()

answer = 0
for i in range(length):
    answer += A[i]*B[i]
print(answer)
