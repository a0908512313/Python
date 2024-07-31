t = int(input())
data = list()
for _ in range(t):
    n = int(input())
    temp = [[[0] for _ in range(n)] for _ in range(2)]
    a, b = input().split()
    for i in range(len(a)):
        if a[i] == '.':
            temp[i][0] = 0
        else:
            temp[i][0] = 1
    for i in range(len(b)):
        if a[i] == '.':
            temp[i][1] = 0
        else:
            temp[i][1] = 1
    data.append(temp)
