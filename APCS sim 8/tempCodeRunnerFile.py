def left(grid):
    n = len(grid)
    transposed_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed_grid[i][j] = grid[j][i]
    for i in range(n):
        transposed_grid[i].reverse()
    return transposed_grid


def right(grid):
    n = len(grid)
    transposed_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed_grid[i][j] = grid[j][i]
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

    y += 1
    if y == n:
        x += 1
        y = 0

    total += grid[x][y]

print(total)
