n = int(input())
actions = list()
for _ in range(n):
    actions.append(int(input()))
data = [0, 0, 0, 0, 0]
index = 0
for action in actions:
    if action == 0:
        print(data[index])
    elif action == 1:
        data[index] += 1
    elif action == 2:
        if index == 4:
            index = 0
        else:
            index += 1
    elif action == 3:
        if index == 0:
            index = 4
        else:
            index -= 1
