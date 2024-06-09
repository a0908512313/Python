k = int(input())
maxScore, time, error = 0,0,0
for i in range(k):
    t, s = [map(int, input().split())]
    if s > maxScore:
        maxScore = s
        time = t
    if s == -1:
        error += 1
ans = maxScore - k - error*2
if ans < 0:
    ans = 0
print(ans, time)
