A, B = map(int, input().split())
a = min(A, B)
b = max(A, B)
case2 = 0
case3 = 0
for i in range(a, b+1):
    print(i)
    if i%2==0:
        case2+=1
    elif i%3==0:
        case3+=1
print(str(case2)+' '+str(case3))
