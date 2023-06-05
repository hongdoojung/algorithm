def main():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)

    mini = 0
    maxi = trees[0]
    if m == 0:
        print(0)
        return
    
    while True:
        result = 0
        height = int((mini + maxi) / 2)
        for tree in trees:
            current = max(tree - height, 0)
            if current == 0:
                break
            result += current
            if result > m:
                break
        if result > m:
            mini = height
        elif result < m:
            maxi = height
        else:
            print(height)
            return
        if maxi - mini <= 1:
            for tree in trees:
                current = max(tree - mini, 0)
                if current == 0:
                    break
                result += current
                if result > m:
                    break
            if result >= m:
                print(mini)
            else:
                print(maxi)
            return


if __name__ == "__main__":
    main()
