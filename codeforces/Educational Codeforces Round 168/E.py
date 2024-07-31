def will_monocarp_fight(n, q, monster_levels, queries):
    results = []

    for i, x in queries:
        i -= 1  # 轉換為 0 索引
        k = x
        monster_level = monster_levels[i]

        # 確定 Monocarp 在第 i 場戰鬥時的等級
        # Monocarp 在第 i 場戰鬥前打了 i 場戰鬥，每 k 場升級一次
        # 計算 Monocarp 的等級
        level = (i // k) + 1

        if level > monster_level:
            results.append("YES")
        else:
            results.append("NO")

    return results


# 讀取輸入
n, q = map(int, input().split())
monster_levels = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# 處理查詢並輸出結果
results = will_monocarp_fight(n, q, monster_levels, queries)
for result in results:
    print(result)
