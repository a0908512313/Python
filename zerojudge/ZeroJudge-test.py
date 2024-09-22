INPUT = list()
while True:
    i = input()
    if i == '0':
        break
    INPUT.append(i)

data = list()

for i in range(len(INPUT) // 2):
    LEN = int(INPUT[i][0])
    temp = map(int, INPUT[i][1])
    add = list()
    add.append(LEN)
    add.append(temp)
    data.append(add)

for i in range(len(data)):
    data[i][1].sort()
    result = 0
    if len(data[i][1]) % 2 == 0:
        for j in range(len(data[i][1]) % 2):
            result += (data[i][1][j] + data[i][1][j])
        print(result)
    else:
        for j in range((len(data[i][1])-1) % 2):
            result += (data[i][1][j] + data[i][1][j])
            result += data[i][1][-1]
        print(result)
