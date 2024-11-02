n = int(input())
result = []
for _ in range(n):
    m = int(input())
    data = list(map(int, input().split()))
    check = True
    for i in range(m - 1):
        if abs(data[i] - data[i+1]) not in [5, 7]:
            check = False
            break
    if check:
        result.append("YES")
    else:
        result.append("NO")

for res in result:
    print(res)
