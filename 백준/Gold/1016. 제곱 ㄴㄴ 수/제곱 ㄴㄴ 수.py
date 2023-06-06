import sys


def get_primes(n):
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1
    
    primes = []
    for index, item in enumerate(arr):
        if item:
            primes.append(index)
    return primes


def main():
    mini, maxi = list(map(int, sys.stdin.readline().split()))

    answer = maxi - mini + 1
    primes = get_primes(int(maxi**0.5+1))
    divisibleByTheSquare = [False] * (maxi-mini+1)

    for i in primes:
        square = i**2
        for j in range(((max(mini, 2) - 1)//square+1) * square, maxi + 1, square):
            # print("process", i, j, len(divisibleByTheSquare))
            if not divisibleByTheSquare[j-mini] :
                divisibleByTheSquare[j-mini] = True
                answer -= 1
                # print("catch", i, j)
        # print(divisibleByTheSquare, primes)
    print(answer)


if __name__ == "__main__":
    main()
