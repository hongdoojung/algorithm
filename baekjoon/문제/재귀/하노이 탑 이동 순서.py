def hanoi_with_logs(n, start, end, logs):
    if n == 1 :
        logs.append((start, end,))
    else:       
        hanoi_with_logs(n-1, start, 6-start-end, logs)
        logs.append((start, end,))
        hanoi_with_logs(n-1, 6-start-end, end, logs)

logs = []
n = int(input())
hanoi_with_logs(n, 1, 3, logs)

print(len(logs))
for x, y in logs:
    print(f"{x} {y}")
