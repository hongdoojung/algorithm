# 문제
# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

# 출력
# 문제의 조건을 만족하는 쌍의 개수를 출력한다.

# 예제 입력 1 
# 9
# 5 12 7 10 9 1 2 3 11
# 13
# 예제 출력 1 
# 3
# 출처
# Olympiad > Balkan Olympiad in Informatics > Junior Balkan Olympiad in Informatics > JBOI 2008 6번

# 데이터를 추가한 사람: BaaaaaaaaaaarkingDog
# 문제를 번역한 사람: baekjoon

import sys

def main():
    how_many = int(input())
    array = list(map(int, input().split()))
    target = int(input())

    result = 0
    array.sort()
    start = 0
    end = how_many - 1

    while start < end:
        if array[start] + array[end] == target:
            result += 1
            start += 1
            end -= 1
        elif array[start] + array[end] > target:
            end -= 1
        elif array[start] + array[end] < target:
            start += 1
    print(result)

if __name__ == "__main__":
    main()
