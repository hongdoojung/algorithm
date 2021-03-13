def is_cross(a, b, lines):
    if a[0] < b[0] and a[1] < b[1]:
        return False
    elif a[0] > b[0] and a[1] > b[1]:
        return False
    else:
        return True

def get_max_lines(lines):
    return 0

how_many = int(input())
lines = {}
for i in range(how_many):
    line = map(int, input().split())
    lines.update({line[0]:line[1]})

print(get_max_lines(lines))
