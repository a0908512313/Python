n = int(input())
actions = [list(input().split()) for _ in range(n)]
m = input()
m_after = m
m_copy = m

for action in actions:
    action_code = action[0]

    if action_code == "search":
        s = action[1]
        count = m.count(s)
        print(count)

    elif action_code == "replace":
        s, r = action[1], action[2]
        m_copy = m
        m = m.replace(s, r)
        m_after = m

    elif action_code == "undo":
        m = m_copy

    elif action_code == "redo":
        m = m_after
