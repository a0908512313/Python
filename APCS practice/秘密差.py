INPUT = input()
first = 0
second = 0
i = 0
while i <= len(INPUT) - 2:
    first += int(INPUT[i])
    second += int(INPUT[i+1])
    i += 1

print(abs(first - second))
