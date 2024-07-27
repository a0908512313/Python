t = int(input())
result = []

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    if (data.count(max(data))) % 2 != 0:
        result.append("yes")
    else:
        result.append("no")

for i in result:
    print(i)
