n = int(input())
MAX, MIN = 0,0
x1, y1 = [map(int, input().split())]
for i in range(n - 1):
    x2, y2 = [map(int, input().split())]
    temp = abs(x2 - x1) + abs(y2 - y1)
    MAX = max(temp, MAX)
    MIN = min(temp, MIN)
    x1, y1 = x2, y2
print(MAX, MIN)
