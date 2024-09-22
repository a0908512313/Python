n = int(input())
data = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
data.sort(reverse=True, key=lambda x: x[-1])

temp = list()
for i in data:
    first = i[0]
    second = i[1]
    temp.append(tuple([int(i) for i in range(first, second+1)]))
start, end = float('inf'), 0
for i in data:
    start = min(start, i[0])
    end = max(end, i[1])
time = set(range(start, end+1))
result = 0

for i in range(len(temp)):
    j = set(temp[i])
    if j.issubset(time):
        time -= j
        result += data[i][-1]

print(result)
