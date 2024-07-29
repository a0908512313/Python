n, m = map(int, input().split())

grid = [[0 for _ in range(m)]for _ in range(n)]
x, y = n//2, m//2
direction = 0
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
count = 0
i = int()
for i in range(10**6):
    if grid[x][y] == 0:
        grid[x][y] = 1
        count += 1
        x += dir[direction][0]
        y += dir[direction][1]
    else:
        direction = (direction - 1) % 4
        x += dir[direction][0]
        y += dir[direction][1]
        if grid[x][y] == 1:
            grid[x][y] = 0
            count -= 1
    if x < 0 or x >= n or y < 0 or y >= m:
        break

print(i)
print(count)
