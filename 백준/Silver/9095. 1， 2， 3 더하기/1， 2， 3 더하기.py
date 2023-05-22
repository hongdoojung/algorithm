import sys


def calculate(x, answer_dict):
    if answer_dict.get(x):
        return answer_dict[x]
    else:
        p, q, r = calculate(x-1, answer_dict), calculate(x-2, answer_dict), calculate(x-3, answer_dict)
        answer_dict.update({x : p + q + r})
        return p + q + r


def main():
    T = int(sys.stdin.readline())
    cases = []
    answer_dict = {
        1 : 1,
        2 : 2,
        3 : 4
    }
    for i in range(T):
        cases.append(int(sys.stdin.readline()))

    for case in cases:
        answer = calculate(case, answer_dict)
        print(answer)


if __name__ == "__main__":
    main()
