import sys

x = sys.stdin.readline()
array = list(map(int, sys.stdin.readline().split()))
array.sort()
print(array[0] * array[-1])