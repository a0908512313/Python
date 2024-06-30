n = int(input())
for _ in range(n):
    INPUT = input().split()
    data = []*3
    data[0] = int(INPUT[0])
    data[1] = int(INPUT[1])
    data[2] = int(INPUT[2])
    temp = min(data)
    tempDIS = []
    while temp <= max(data):
        dis = abs(temp - data[0]) + abs(temp - data[1]) + abs(temp - data[2])
        tempDIS.append(dis)
        temp += 1
    index = tempDIS.index(max(tempDIS))
    print(min(data) + index)
