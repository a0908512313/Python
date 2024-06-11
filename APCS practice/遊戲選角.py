n = int(input())
first, second, x1, x2, y1, y2 = 0, 0, 0, 0, 0, 0
for _ in range(n):
    INPUT = input().split()
    x, y = int(INPUT[0]), int(INPUT[1])
    p = x**2 + y**2
    if (p > first):
        second = first
        first = p
        x1 = x
        y1 = y
    elif (p > second):
        second = p
        x2 = x
        y2 = y
print(str(x)+" "+str(y)+" ")
