n = int(input())
datas = list()
for _ in range(n):
    datas.append(int(input()))
result = list()

for data in datas:
    if data % 33 == 0:
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)
