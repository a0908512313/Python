X = input()
STR = ''
a, b, c = X[0], X[1], X[2]
if a == b == c == 0:
    STR+='0'
else:
    if a == 0:
        STR+="1"
    elif b == 0:
        STR +='2'
    elif c==0:
        STR+='3'
print(STR)
