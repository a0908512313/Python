R, C, M = map(int, input().split())
data = list()
for _ in range(R):
    temp = list(map(int, input().split()))
    data.append(temp)
move = list(map(int, input().split()))


def mir(data):
    return data[::-1]


def rotate(data):
    row = len(data)
    col = len(data[0])
    temp = [[0 for _ in range(row) for _ in range(col)]]
    for i in range(row):
        for j in range(col):
            temp[j][row - 1 - i] = data[i][j]
    return temp


for i in move:
    if i == 1:
        data = mir(data)
    else:
        data = rotate(data)

row = len(data)
col = len(data[0])
print(row, col)
for i in data:
    print(' '.join(map(str, i)))
