# 讀取輸入
n, t, p = map(int, input().split())
data = list(map(int, input().split()))
count = 0
for i in data:
    if i >= t:
        count += 1

if count >= p:
    print(0)
else:
    temp = list()
    for i in data:
        if i < t:
            temp.append(i)
        temp.sort(reverse=True)
    need = p - count
    print(abs(temp[need - 1] - t))
