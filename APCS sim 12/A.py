t = int(input())
ns = list()
for _ in range(t):
    ns.append(int(input()))
results = list()
for n in ns:
    count = 0
    for a in range(1, n-2):
        for b in range(a + 1, n-1):
            for c in range(b + 1, n):
                if a + b >= c:
                    count += 1
    results.append(count)
for i in results:
    print(i)
