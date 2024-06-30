n = int(input())
init = [map(int, input().split())]
init.sort()
STR = ''

for i in range(n):
    STR += str(init[i]) + " "
PASS = []
NOT = []
for i in range(n):
    if init[n] >= 60:
        PASS.append(init[n])
    elif init[n] < 60:
        NOT.append(init[n])
print(init)

if len(NOT) == 0:
    print("best case")
else:
    print(max(NOT))


if len(PASS) == 0:
    print("worst case")
else:
    print(min(PASS))
