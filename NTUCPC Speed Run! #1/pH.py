n, k = map(int, input().split())
data = []
for _ in range(n):
    s, f, c = map(int, input().split())
    data.append((s, f, c))
remain = []
for s, f, c in data:
    if f > s:
        remain.append((f - s, c))
remain.sort(key=lambda x: x[1])
current_score = sum(s for s, _, _ in data)
need = k - current_score
result = 0
if need <= 0:
    print(0)
else:
    index = 0
    while need > 0 and index < len(remain):
        can, MIN = remain[index]
        if need >= can:
            result += can * MIN
            need -= can
        else:
            result += need * MIN
            break
        index += 1
    print(result)
