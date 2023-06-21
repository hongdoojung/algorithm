import sys


x, y, w, h = map(int, sys.stdin.readline().split())

height = min(h - y , y)
width = min(w - x , x)
print(min(height, width))
