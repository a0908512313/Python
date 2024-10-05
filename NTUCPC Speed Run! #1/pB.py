n, m = map(int, input().split())
grid = list()
for _ in range(n):
    temp = list(map(int, input()))
    grid.append(temp)
count = 0
for i in range(n - 2):
    for j in range(m-1):
        if (grid[i][j] == grid[i+1][j] == grid[i][j+1] == 0 and
            grid[i+1][j+1] == grid[i+2][j+1] == 1) or\
            (grid[i][j] == grid[i][j+1] == grid[i+1][j+1] == 0 and
             grid[i+1][j] == grid[i+2][j] == 1):
            count += 1
print(count)
