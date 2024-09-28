n = int(input())
data = [i for i in range(1, n + 1)]
moves = []

while True:
    temp = list(map(int, input().split()))
    if temp[0] == 3:
        break
    moves.append(temp)

for move in moves:
    if move[0] == 1:
        a, b = move[1], move[2]
        index = data.index(b)
        data.remove(a)
        data.insert(index, a)
    elif move[0] == 2:
        p = move[1]
        print(data[p - 1])
