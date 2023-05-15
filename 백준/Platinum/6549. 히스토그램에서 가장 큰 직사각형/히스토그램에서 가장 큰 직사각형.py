def main(how_many, array):
    stack = [0]
    greatest = 0

    for i in range(1, how_many):
        cursor = i
        if array[stack[-1]] < array[i]:
            pass
        else:    
            while stack and array[i] < array[stack[-1]]:
                cursor = stack.pop()
                left = stack[-1] + 1 if stack else 0
                greatest = max(greatest, (i - left) * array[cursor])
        stack.append(i)

    while stack:
        cursor = stack.pop()
        left = stack[-1] + 1 if stack else 0
        greatest = max(greatest, (how_many - left) * array[cursor])
    
    print(greatest)


if __name__ == "__main__":
    arrays = []

    while True:
        array = list(map(int, input().split()))
        if array == [0]:
            break
        arrays.append(array[1:])

    for array in arrays:
        main(len(array), array)
