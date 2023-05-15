def main():
    length = int(input())
    cases = []
    for i in range(length):
        cases.append(input())
    for case in cases:
        while case:
            if case[:3] == "100":
                x = 3
                while len(case) >= x + 1 and case[x] == "0":
                    x += 1
                if not case[x:] or case[x] != "1":
                    break
                while len(case) >= x + 1 and case[x] == "1":
                    x += 1
                if case[x - 1 : x + 2] == "100" and case[x - 2] == "1":
                    case = case[x - 1:]
                else:
                    case = case[x:]
            elif case[:2] == "01":
                x = 2
                while case[x:x + 2] == "01":
                    x += 2
                case = case[x:]
            else:
                break
        if case:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()
