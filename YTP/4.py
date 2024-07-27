t = int(input())
result = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = 0
    while i < n - 1:
        if a[i] >= a[i + 1] and b[i] >= b[i + 1]:
            a.pop(i + 1)
            b.pop(i + 1)
            n -= 1
        else:
            i += 1

    result.append(n)

for i in result:
    print(i)
