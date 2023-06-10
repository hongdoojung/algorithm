import sys
import heapq


def main():
    how_many = int(sys.stdin.readline())
    for _ in range(how_many):
        max_q = []
        min_q = []
        push = 0
        max_pop = 0
        min_pop = 0
        check_dict = {}
        how_long_case = int(sys.stdin.readline())
        for __ in range(how_long_case):
            command, i = (sys.stdin.readline().split())
            if command == "I":
                inti = int(i)
                heapq.heappush(max_q, -1*inti)
                heapq.heappush(min_q, inti)
                check_dict.update({inti: check_dict.get(inti, 0) + 1})
                push += 1
            elif command == "D" and push > min_pop + max_pop:
                if i == "1":
                    while True:
                        pop = -1*heapq.heappop(max_q)
                        if check_dict.get(pop, 0):
                            check_dict.update({pop: check_dict[pop] -1})
                            max_pop += 1
                            break
                elif i == "-1":
                    while True:
                        pop = heapq.heappop(min_q)
                        if check_dict.get(pop, 0):
                            check_dict.update({pop: check_dict[pop] -1})
                            min_pop += 1
                            break
        #     print(max_q, min_q, max_pop, min_pop, check_dict)
        # print(max_q, min_q)
        if push > min_pop + max_pop:
            while True:
                pop = -1*heapq.heappop(max_q)
                if check_dict.get(pop, 0):
                    check_dict.update({pop: check_dict[pop] -1})
                    max_pop += 1
                    break
            pop1 = pop
            if push > min_pop + max_pop:
                while True:
                    pop = heapq.heappop(min_q)
                    if check_dict.get(pop, 0):
                        check_dict.update({pop: check_dict[pop] -1})
                        min_pop += 1
                        break
                pop2 = pop
                print(f"{pop1} {pop2}")
            else:
                print(f"{pop1} {pop1}")
        else:
            print("EMPTY")

if __name__ == "__main__":
    main()
