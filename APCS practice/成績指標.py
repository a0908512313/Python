n = int(input())
data = list(map(int, input().split()))
data.sort()
print(' '.join(map(str, data)))
more, less = list(), list()
for i in data:
    if i >= 60:
        more.append(i)
    else:
        less.append(i)

print(max(less) if len(less) > 0 else ('best case'))
print(min(more) if len(more) > 0 else ('worst case'))
