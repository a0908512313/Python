a = [1, 2, 3]
b = [1, 2, 4]
result = 0
for i in range(len(a)):
    if b[i] in a[i]:
        result += 1
