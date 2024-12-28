n, m, q = map(int, input().split())
table = [None] * 9
recipes = list()  # 1 for mode 2 for type 3 for count per action
items = list()
actions = list()
results = list()

for _ in range(n):
    temp = list()
    for _ in range(4):
        temp.append(list(map(int, input().split)))

for _ in range(1):
    tempItemList = list(map(int, input().split()))
    for i in range(0, m, 2):
        items.append([tempItemList[i], tempItemList[i+1]])

for _ in range(q):
    actions.append(list(input().split()))

for action in actions:
    if action[0] == 'put':
        i, p, c = action[1:]
        if table[c][0] == items[i]:
            table[c][1] += p
        elif table[c][0] != items[i]:
            for i in items:
                if i[0] == table[c]:
                    i[0] += table[c][1]
                    found = True
            if not found:
                items.append(table[c])
            table[c] = [items[i], p]
        else:
            table[c] = [items[i], p]
        items[i][1] -= p

    elif action[0] == 'return':
        p = action[1]
        if not table[p-1] == None:
            pass
        else:
            for item in items:
                if item[0] == table[p][0]:
                    item[1] += table[p][1]
                    table[p] = None
    elif action[0] == 'craft':
        pass
