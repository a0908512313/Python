a, b, c = map(int, input().split())
if a > 1:
    a = 1
if b > 1:
    b = 1
test = False
if (a and b) == c:
    print('AND')
    test = True
if (a or b) == c:
    print('OR')
    test = True
if (a and not b) or (not a and b) == c:
    print('XOR')
    test = True
if not test:
    print('IMPOSSIBLE')
