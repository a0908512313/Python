n = int(input())
name, IN, OU = list(), list(), list()
for _ in range(n):
    temp = input().split()
    name.append(temp[0])
    IN.append(temp[1])
    OU.append(temp[2])
k = int(input())
QUE = input()
que = list()
for i in QUE:
    que.append(i)
result = list()

for i in range(1, k):
    if IN[name.index(que[i])] == OU[name.index(que[i - 1])]:
        result.append(1)
    else:
        result.append(0)
for i in result:
    print(i)
