block = list()
for _ in range(9):
    temp = list(map(int, input().split()))
    block.append(temp)
pic = list()
for _ in range(9):
    pic.append(input())
vertical = list()
lateral = list()
for i in range(9):
    tempv, templ = list(), list()
    for j in range(9):
        tempv.append(pic[j][i])
        templ.append(pic[i][j])
    vertical.append(tempv)
    lateral.append(templ)
if any(i.count("*") > 2 for i in vertical) or any(i.count("*") > 2 for i in lateral):
    print("Invalid")
else:
    status = {i: 0 for i in range(1, 10)}
    for i in range(9):
        for j in range(9):
            if pic[i][j] == "*":
                status[block[i][j]] += 1
                if status[block[i][j]] > 2:
                    print("Invalid")
                    break
    print("Valid")
