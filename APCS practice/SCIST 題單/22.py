N, P, X, Y = map(int, input().split())
total = 0
read = 0
while read < P:
    if(read + 1) % N == 0:
        total += Y
    else:
        total += X

    if read == P  and (page + 1)%N == 0:
        total+= Y
print(total)
