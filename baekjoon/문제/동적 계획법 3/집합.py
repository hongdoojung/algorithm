import sys

LENGTH = 20

def add(num, bitmask):
    return bitmask if bitmask & 2**num else bitmask + 2**num
    
def remove(num, bitmask):
    return bitmask - 2**num if bitmask & 2**num else bitmask

def check(num, bitmask):
    print(1 if (bitmask&2**num) else 0)

def toggle(num, bitmask):
    return bitmask - 2**num if bitmask & 2**num else bitmask + 2**num
    
def all(bitmask):
    return 2**(LENGTH+1) - 1

def empty(bitmask):
    return 0

def main():
    bitmask = 0
    operations = int(input())
    
    for i in range(operations):
        line = sys.stdin.readline()
        if line.startswith("add"):
            bitmask = add(int(line.split(" ")[1])-1, bitmask)
        elif line.startswith("remove"):
            bitmask = remove(int(line.split(" ")[1])-1, bitmask)
        elif line.startswith("check"):
            check(int(line.split(" ")[1])-1, bitmask)
        elif line.startswith("toggle"):
            bitmask = toggle(int(line.split(" ")[1])-1, bitmask)
        elif line.startswith("all"):
            bitmask = all(bitmask)
        elif line.startswith("empty"):
            bitmask = empty(bitmask)

if __name__ == "__main__":
    main()
