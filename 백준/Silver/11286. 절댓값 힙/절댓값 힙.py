import sys
import heapq

def main():
    how_many = int(sys.stdin.readline())
    array = []
    same_values = {}
    heap = []
    for i in range(how_many):
        num = int(sys.stdin.readline())
        array.append(num)
    # print("----")
    for num in array:
        # print(11111, heap, same_values, num)
        if num == 0:
            if heap:
                abs_num = heapq.heappop(heap)
                # print(22222, abs_num, same_values[abs_num])
                if same_values[abs_num][0]:
                    same_values[abs_num][0] -= 1
                    print(-abs_num)
                else:
                    same_values[abs_num][1] -= 1
                    print(abs_num)
            else:
                print(0)
        else:
            if num < 0:
                index = 0
            else:
                index = 1
            abs_num = abs(num)
            new_info = same_values.get(abs_num, [0, 0])
            new_info[index] += 1
            same_values.update({abs_num : new_info})
            heapq.heappush(heap, abs_num)


if __name__ == "__main__":
    main()
