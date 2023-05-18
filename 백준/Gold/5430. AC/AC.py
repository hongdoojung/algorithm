def main():
    how_many_cases = int(input())
    cases = []
    for i in range(how_many_cases):
        commands = input()
        numbers = int(input())
        if numbers:
            array = list(map(int, input()[1:-1].split(",")))
        else:
            input()
            array = []
        cases.append([commands, array])
    for commands, array in cases:
        is_left = True
        left = 0
        right = 0
        for stri in commands:
            if stri == "R":
                is_left = not is_left
            else:
                if is_left:
                    left += 1
                else:
                    right += 1
        if left + right > len(array):
            print("error")
        else:
            if is_left:
                answer = (array[left:len(array) - right])
            else:
                array.reverse()
                answer = (array[right:len(array) - left])
            stranswer = ','.join(map(str,answer))
            print('['+stranswer+']')


if __name__ == "__main__":
    main()
