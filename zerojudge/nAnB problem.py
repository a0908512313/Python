temp = list()
while True:
    try:
        TEMP = input().strip()
        if TEMP:
            temp.append(TEMP)
    except EOFError:
        break

i = 0
data = list()  # case correct time attempt
while i < len(temp):
    correct = temp[i]  # correct
    i += 1
    n = int(temp[i])  # time
    i += 1
    attempts = list()  # attempts
    for _ in range(n):
        attempts.append(temp[i])
        i += 1

    TEMP = [correct, n, attempts]
    data.append(TEMP)
    if i < len(temp) and not temp[i]:
        i += 1

for case in data:
    cor = list(map(int, case[0].split()))
    attempts = [list(map(int, attempt.split())) for attempt in case[2]]
    LEN = len(cor)

    for attempt in attempts:
        a, b = 0, 0
        used_correct = [False] * LEN
        cor_count = [0] * 10  # 0-9的數字計數器

        # 第一輪檢查正確位置
        for j in range(LEN):
            if cor[j] == attempt[j]:
                a += 1
                used_correct[j] = True
            else:
                cor_count[cor[j]] += 1  # 計算正確密碼的數字

        # 第二輪檢查正確數字但不在正確位置
        for j in range(LEN):
            if not used_correct[j]:  # 如果這個嘗試的數字還沒有在正確位置
                if cor_count[attempt[j]] > 0:  # 檢查是否存在此數字
                    b += 1
                    cor_count[attempt[j]] -= 1  # 使用此數字

        print(f'{a}A{b}B')
