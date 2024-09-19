n = int(input())
data = list()
N = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
data.sort(key=lambda x: x[0])
i = 0
j = 1
while j < n:
    FL, FR = data[i][0], data[i][1]
    RL, RR = data[j][0], data[j][1]
    if RL > FR:
        N.append(data[i])
        i = j
    else:
        data[i][1] = max(FR, RR)
    j += 1
N.append(data[i])
result = 0
for i in N:
    result += (i[1] - i[0])
print(result)
