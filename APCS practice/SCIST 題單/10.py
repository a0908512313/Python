a, b, c, d, e = [int(i) for i in input().split()]
first = (b - a) * c
plus = 0
second = plus * e
while(second < first):
    plus += 1
    second = plus * e
print(d + plus)
