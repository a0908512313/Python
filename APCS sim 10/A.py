n, m = map(int, input().split())
course = [0 for _ in range(m)]
actions = list()
for _ in range(n):
    actions.append(list(map(int, input().split())))
for action in actions:
    a, b, c = action[0], action[1], action[2] - 1
    if a == 1:
        course[c] += b
    elif a == 2:
        if course[c] > b:
            course[c] -= b
        else:
            course[c] = 0
print(' '.join(map(str, course)))
