n = int(input())
result = list()
cases = list()
for _ in range(n):
    t = int(input())
    data = list(map(int, input().split()))
    cases.append(data)
for case in cases:
    case.sort()
    while len(case) > 1:
        first = case.pop(0)
        second = case.pop(0)
        avg = (first + second) // 2
        case.insert(0, avg)
        case.sort()
    result.append(case[0])
print(" ".join(map(str, result)))
