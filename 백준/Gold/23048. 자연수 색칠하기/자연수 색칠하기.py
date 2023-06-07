import sys


def get_primes(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    
    primes = []
    for index, item in enumerate(arr):
        if item:
            primes.append(index)
    return primes


def main():
    n = int(sys.stdin.readline())
    primes = get_primes(n)
    k = 2
    arr = [1] * (n + 1)

    # print(primes)
    for prime in primes:
        arr[prime] = k
        j = 2
        while (prime * j) <= n:
            arr[prime*j] = k
            j += 1
        k += 1
        
    print(len(primes) + 1)
    # print(arr)
    stranswer = ' '.join(map(str,arr[1:]))
    print(stranswer)


if __name__ == "__main__":
    main()
