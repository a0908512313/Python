n = int(input())
cards = list()
while n > 0:
    temp = list(map(int, input().split()))
    n -= len(temp)
    cards.extend(temp)
count = [0] * 52
for i in cards:
    count[i-1] += 1
first, second = 0, 0
first = min(count)
MAX = max(count)
for i in range(52):
    if count[i] < MAX:
        second += (MAX - count[i])

print(first, second)
