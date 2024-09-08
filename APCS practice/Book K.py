N, M, K = map(int, input().split())
role = [int(i) for i in range(1, N+1)]
pos = 0
m = M - 1
for i in range(K):
    pos += M
    if pos >= len(role):
        pos -= len(role)
    role.pop(pos)
if pos >= len(role):
    pos -= len(role)
print(role[pos])
