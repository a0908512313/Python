K = int(input())
max_pieces = 0
for k in range(K+1):
    h = k
    v = K-k
    pieces = (h+1)*(v+1)
    max_pieces = max(max_pieces, pieces)
print(max_pieces)
