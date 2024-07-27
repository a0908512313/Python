import numpy as np
m, n, p = map(int, input().split())


def alice_win_probability(m, n, p):
    # 初始化狀態
    states = np.zeros((m + 1, n + 1))
    # 初始條件
    states[0, :] = 0   # Alice沒錢了，機率為0
    states[:, 0] = 1   # Bob沒錢了，Alice贏光了，機率為1

    # 計算轉移機率
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            states[i, j] = p * states[i, j - 1] + (1 - p) * states[i - 1, j]

    return states[m, n]


print(alice_win_probability(m, n, p))
