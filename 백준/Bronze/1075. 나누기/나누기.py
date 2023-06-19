import sys

a = sys.stdin.readline().strip("\n")
b = sys.stdin.readline().strip("\n")
a = a[:-2] + "00"
remainder = int(a)%int(b)
if remainder:
    print(str(int(a) + int(b) - remainder)[-2:])
else:
    print(a[-2:])
