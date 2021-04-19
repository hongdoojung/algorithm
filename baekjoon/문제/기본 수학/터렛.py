def get_length_square(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2) ** (1/2)

how_many = int(input())
lines = []
for i in range(how_many):
    lines.append(input().split())

for line in lines:
    line = list(map(int,line))
    if line[2] < line[5]:
        small_circle = (line[0], line[1], line[2])
        large_circle = (line[3], line[4], line[5])
    else:
        small_circle = (line[3], line[4], line[5])
        large_circle = (line[0], line[1], line[2])

    if small_circle == large_circle:
        print(-1)
        continue

    length = get_length_square(small_circle[0], small_circle[1], large_circle[0], large_circle[1])
    if length <= large_circle[2]:
        if length + small_circle[2] == large_circle[2]:
            print(1)
            continue
        elif length + small_circle[2] < large_circle[2]:
            print(0)
            continue
        else:
            print(2)
            continue
    else:
        if length == large_circle[2] + small_circle[2]:
            print(1)
            continue
        if length > large_circle[2] + small_circle[2]:
            print(0)
            continue
        else:
            print(2)
            continue
