R, C, M = map(int, input().split())
data = list()
for _ in range(R):
    temp = list(map(int, input().split()))
    data.append(temp)
move = list(map(int, input().split()))


def mir(data):
    def swap(data: list, a, b):
        temp = data[a]
        data[a] = data[b]
        data[b] = temp
        return data

    for i in range(len(data) if data % 2 == 0 else (len(data) - 1) // 2):
        swap(data, i, len(data) - 1 - i)
    return data


def rotate(data):
    temp = [len(data[0])][len(data)]
    for i in range(len(data)):
        for j in range(len(data[0])):
            temp[i][j] = temp[j][len(data) - 1 - i]
    return temp


for i in move:
    if i == 1:
        data = mir(data)
    elif i == 2:
        data = rotate(data)

row = len(data)
col = len(data[0])
print(row, col)
for i in data:
    temp = i.join(' ')
    print(temp)
