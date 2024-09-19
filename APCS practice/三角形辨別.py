data = list(map(int, input().split()))
data.sort()
print(' '.join(map(str, data)))
a = data[0] + data[1]
b = data[2]
if a < b:
    print('No')
else:
    a = (data[0] * data[0]) + (data[1] * data[1])
    b = data[2] * data[2]
    if a < b:
        print('Obtuse')
    elif a == b:
        print('Right')
    elif a > b:
        print('Acute')
