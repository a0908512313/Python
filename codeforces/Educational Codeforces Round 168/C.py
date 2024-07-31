t = int(input())
data = list()
for _ in range(t):
    temp = list()
    temp.append(int(input()))
    temp.append(input())
    data.append(temp)


def min_cost_rbs(t, test_cases):
    results = []

    for case in test_cases:
        n, s = case
        opening_positions = [i for i in range(1, n, 2)]
        cost = 0
        stack = []

        for i in range(1, n, 2):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    open_pos = stack.pop()
                    cost += i - open_pos

        results.append(cost)

    return results


result = min_cost_rbs(t, data)
for i in result:
    print(i)
