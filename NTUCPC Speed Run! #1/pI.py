# 走一排+x
# 到隔壁
# 空y0
# 有人y1

n, l, r, m = map(int, input().split())
x, y0, y1 = map(int, input().split())
data = []

for _ in range(m):
    data.append(list(map(int, input().split())))

result = 0
seat = [[0 for _ in range(l + r)] for _ in range(n)]

for passenger in data:
    col = passenger[0] - 1
    position = passenger[1]

    if position > 0:
        position += l - 1
        for i in range(l, position + 1):
            if 0 <= col < n and 0 <= i < len(seat[col]):
                if seat[col][i] == 1:
                    result += y1
                else:
                    result += y0
        if 0 <= position < len(seat[col]):
            seat[col][position] = 1

    elif position < 0:
        position += l
        for i in range(l - 1, position - 1, -1):
            if 0 <= col < n and 0 <= i < len(seat[col]):
                if seat[col][i] == 1:
                    result += y1
                else:
                    result += y0
        if 0 <= position < len(seat[col]):
            seat[col][position] = 1

print(result)
