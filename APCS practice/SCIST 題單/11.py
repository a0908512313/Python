a = int(input())
LIST = list()
for _ in range(a):
    LIST.append(int(input()))

LIST2 = list()
for i in range(a):
    temp = 400
    j = 1
    while(temp < LIST[i]):
        temp+=400
        j+=1
    LIST2.append(j)
    temp = 400
    j = 1

for i in range(len(LIST2)):
    print(LIST2[i])
