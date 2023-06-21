x = int(input())

controled_x = min(100, x)
answer = controled_x
if controled_x == 100:
    answer -= 1

if controled_x == 100:
    for i in range(controled_x, x + 1):
        stri = str(i)
        # print(stri)
        a = int(stri[0]) - int(stri[1])
        b = int(stri[1]) - int(stri[2])
        if a == b:
            answer += 1

print(answer)
