import sys

table = {
    "black":0,
    "brown":1,
    "red":2,
    "orange":3,
    "yellow":4,
    "green":5,
    "blue":6,
    "violet":7,
    "grey":8,
    "white":9,
}

a = sys.stdin.readline().strip("\n")
b = sys.stdin.readline().strip("\n")
c = sys.stdin.readline().strip("\n")

print(int((str(table[a])+str(table[b])))*10**table[c])
