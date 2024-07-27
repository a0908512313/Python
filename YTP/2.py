n, k = map(int, input().split())
data = list(map(int, input().split()))
lis = list()
temp = list()
for i in data:
    if i not in temp:
        temp.append(i)
temp.sort()
for i in temp:
    for j in temp:
        TEMP = abs(k - (i * j))
        if TEMP in lis:
            pass
        else:
            lis.append(TEMP)
print(min(lis))
