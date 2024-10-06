def solve(n, x, arr):
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    
    for num in range(max(0, mex - x), mex):
        if num in num_set:
            return mex + 1
    
    return mex

t = int(input())
result = []

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    result.append(solve(n, x, arr))

print(" ".join(map(str, result)))