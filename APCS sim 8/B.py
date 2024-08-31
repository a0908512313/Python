def left(grid):
    n = len(grid)
    # 轉置矩陣
    transposed_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed_grid[i][j] = grid[j][i]
    # 反轉每一行
    for row in transposed_grid:
        row.reverse()
    return transposed_grid


def right(grid):
    n = len(grid)
    # 轉置矩陣
    transposed_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed_grid[i][j] = grid[j][i]
    # 反轉每一列
    for j in range(n):
        for i in range(n // 2):
            transposed_grid[i][j], transposed_grid[n - 1 -
                                                   i][j] = transposed_grid[n - 1 - i][j], transposed_grid[i][j]
    return transposed_grid


n = int(input())
directions = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
x, y = 0, 0
total = grid[x][y]

for direction in directions:
    if direction == 0:
        grid = left(grid)
    elif direction == 1:
        grid = right(grid)

    x += 1
    if x == n:
        y += 1
        x = 0

    total += grid[x][y]

print(total)
