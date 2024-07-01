a, b = map(int, input().split())
A, B = False, False
if a%2==0:
    A = True
if b%2==0:
    B = True
if A==B:
    print("yes")
else:
    print("no")
