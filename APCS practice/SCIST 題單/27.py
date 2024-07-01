import itertools

a, b = map(int, input().split())
test = itertools.product(range(1, 7), repeat = a)

temp = []
for i in test:
    temp.append(sum(i))

BOOL = False

for i in temp:
    if i ==  b:
        BOOL = True
        break

if BOOL:
    print("yes")
else:
    print("no")
