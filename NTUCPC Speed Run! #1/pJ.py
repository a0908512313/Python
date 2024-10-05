t = int(input())
cases = []
for _ in range(t):
    cases.append(list(map(int, input().split())))

for case in cases:
    a, b, c, d = case

    if a == 0 or b == 0:
        if c == 0 or d == 0:
            print(">")
        else:
            print("<")
    else:
        first = a**b
        second = c*d
        if first > second:
            print(">")
        elif first == second:
            print("=")
        else:
            print("<")
