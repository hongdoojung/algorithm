def check(x):
    strx = str(x)
    correct = True
    for i in range(len(strx) - 1):
        if int(strx[i]) > int(strx[i + 1]):
            continue
        else:
            correct = False
            break
    return correct, i


def main():
    num = int(input())
    corrects = 9
    x = 10

    if num < 10:
        print(num)
        return
    
    while num > corrects and x < 9876543210:
        strx = str(x)
        correct, i = check(x)
        while correct == False:
            strx = strx[0:i] + str(int(strx[i]) + 1) + "0" * len(strx[i + 1:])
            x = int(strx)
            correct, i = check(x)
        corrects += 1
        x += 1

    # print(x - 1, corrects)
    if x - 1 > 9876543210 or corrects < num:
        print(-1)
    elif x - 1 == 9876543210:
        print(x - 1)
    else:
        print(x - 1)


if __name__ == "__main__":
    main()
