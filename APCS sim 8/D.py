n = int(input())
data = list(map(int, input().split()))
result = 0
for i in range(n - 2):
    for j in range(i + 2, n):
        temp = True
        MAX = max(data[i], data[j])
        for c in range(i + 1, j):
            if data[c] > MAX:
                temp = False
                break
        if temp:
            result += 1
result += (n - 1)
print(result)
