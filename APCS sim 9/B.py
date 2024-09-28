n, m = map(int, input().split())
plate = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    final = list()
    for i in temp:
        TEMP = [i, 0, i]
        final.append(TEMP)
    plate.append(final)

k, q = map(int, input().split())

actions = list()
for _ in range(k + q):
    temp = list(map(int, input().split()))
    actions.append(temp)


def total():
    result = 0
    for i in plate:
        for j in i:
            initial = j[0]
            hit_count = j[1]
            if hit_count > 0:
                t = hit_count * (hit_count + 1) // 2
                result += initial * t
            else:
                result += initial
    return result


def cal(n):
    return n * (n + 1) // 2


def clear():
    for i in plate:
        for j in i:
            j[0] = j[2]
            j[1] = 0


def man(r, c):
    x = max(0, min(r, n - 1))
    y = max(0, min(c, m - 1))
    return abs(r - x) + abs(c - y)


TOTAL = total()
last_hit = None

for action in actions:
    if action[0] == 1:
        x = action[1] - 1
        y = action[2] - 1
        if 0 <= x < n and 0 <= y < m:
            temp = plate[x][y]
            if (x, y) != last_hit:
                last_hit = (x, y)
                temp[0] = temp[2]
                temp[1] = 0
            temp[1] += 1
            temp[0] = temp[2] * cal(temp[1])
        else:
            distance = man(x, y)
            TOTAL -= distance
            clear()
            last_hit = None
    elif action[0] == 2:
        TOTAL = total()
        print(TOTAL)
