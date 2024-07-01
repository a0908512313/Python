a, b, c = map(int, input().split())
main = a*100 + b*10 + c
if main%4 == 0:
    print("YES")
else:
    print("NO")
