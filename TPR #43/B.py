x1, y1, x2, y2 = map(int, input().split())
k = int(input())


def main(x1, y1, x2, y2, k):
    def dx(x):
        return abs(abs(x - x1) - abs(x - x2))

    def dy(y):
        return abs(abs(y - y1) - abs(y - y2))
    found = False
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    for i in range(min_x - k, max_x + k):
        for j in range(min_y - k, max_y + k):
            if dx(i) + dy(j) == k:
                return i, j

    return int(10**9 + 1), int(10**9 + 1)


x, y = main(x1, y1, x2, y2, k)
print(x, y)
