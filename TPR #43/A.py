a, b, k = map(int, input().split())
result = list()
for i in range((min(a, b) - k), (max(a, b) + k + 1)):
    if abs(abs(a - i) - abs(b - i)) == k:
        result.append(i)
        break

if result:
    print(result[0])
else:
    print(int(10**9 + 1))
