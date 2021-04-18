def get_length_square(x0, y0, x1, y1):
    return (x0-x1)**2 + (y0-y1)**2

how_many = int(input())
lines = []
for i in range(how_many):
    lines.append(input().split())


for line in lines:
    
    if line[0] == line[3] and line[1] == line[4] and line[2] == line[5]:
        return -1

    # if lines[2] < lines[5]:
    #     small_circle = (lines[0], lines[1], lines[2])
    #     large_circle = (lines[3], lines[4], lines[5])
    # else:
    #     small_circle = (lines[3], lines[4], lines[5])
    #     large_circle = (lines[0], lines[1], lines[2])

    # if get_length_square(small_circle[0], small_circle[1], large_circle[0], large_circle[1]) < large_circle[2]:

    # length_square = (line[0]-line[3])**2 + (line[1]-line[4])**2
    # diameter_sum_square = (line[2]+line[5])**2

    elif length_square < diameter_sum_square:

