def make_bigger_square(square, level):
    if level == 0:
        return square
    else:
        new_square = []
        for i in range(len(square) * 3):
            new_square.append(["*"] * 3 * len(square))
        for y in range(len(square)):
            for x in range(len(square)):
                if square[y][x] == "*":
                    new_square[y * 3 + 1][x * 3 + 1] = " "
                else:
                    for new_x in range(x * 3, x * 3 + 3):
                        for new_y in range(y * 3, y * 3 + 3):
                            new_square[new_x][new_y] = " "
        return make_bigger_square(new_square, level - 1)

n = int(input())
rows = []

level = 0
while n != 3:
    n /= 3
    level += 1

square = [
    ["*","*","*"],
    ["*"," ","*"],
    ["*","*","*"]
]
new_square = make_bigger_square(square, level)
for row in new_square:
    for item in row:
        print(item, end="")
    print()
