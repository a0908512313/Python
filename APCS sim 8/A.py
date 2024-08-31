n = int(input())
data = []
for i in range(n):
    temp = list(map(int, input().split()))
    temp.insert(0, i+1)
    data.append(temp)

data.sort(reverse=True, key=lambda x: (x[0], x[3]))

for i in data:
    print(' '.join(map(str, i)))
