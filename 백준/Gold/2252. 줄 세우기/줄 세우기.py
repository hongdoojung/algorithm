import sys


N, M = map(int, sys.stdin.readline().split())
array = [1 for i in range(N+1)]
pointing = {}
pointed = {}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a_pointing = pointing.get(a, [])
    a_pointing.append(b)
    pointing[a] = a_pointing
    b_pointed = pointed.get(b, [])
    b_pointed.append(a)
    pointed[b] = b_pointed


q = []
while pointing:
    candidates = pointing.keys()
    for candidate in candidates:
        # print(1)
        if not pointed.get(candidate):
            # print(2, candidate)
            removes = pointing[candidate]
            for remove in removes:
                pointed[remove].remove(candidate)
                if not pointed[remove]:
                    pointed.pop(remove)
            pointing.pop(candidate)
            q.append(candidate)
            array[candidate] = 0
            break
        else:
            continue

# print(1111, )
q.extend([index for index, i in enumerate(array) if i == 1][1:])
stranswer = ' '.join(map(str,q))
print(stranswer)
# print(q)
# print(array)
