t = int(input())
results = []

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    can = False
    for num in num_set:
        if num < mex and (num + x) >= mex:
            can = True
            break

    if can:
        mex += 1

    results.append(mex)

print(' '.join(map(str, results)))
