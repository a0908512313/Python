a = int(input())
if a%9==0:
    a += 9
else:
    a+= 9-(a%9)
print(a)
