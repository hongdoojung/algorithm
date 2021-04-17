x_points = []
y_points = []

for i in range(3):
    line = input().split()
    x_points.append(line[0])
    y_points.append(line[1])

x_points.sort()
y_points.sort()
x_duplicate = x_points[1]
y_duplicate = y_points[1]

for i in range(2):
    x_points.remove(x_duplicate)
    y_points.remove(y_duplicate)

print(x_points[0], y_points[0])
