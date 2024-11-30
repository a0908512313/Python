n, m = map(int, input().split())  # m for self MMR
match_data = [list(map(int, input().split()))
              for _ in range(n)]  # Match data (win/lose, enemy MMR)
result = list()


def calculate_mmr(data, m):
    for match in data:
        enemy_mmr = match[1]
        score_change = int((enemy_mmr - m) * 0.05)

        if match[0] == 0:
            score_change -= 25
            if score_change <= 0:
                m += score_change
        else:
            score_change += 25
            if score_change <= 0:
                m += 1
            else:
                m += score_change
    return m


result.append(calculate_mmr(match_data, m))

for i in range(n):
    if match_data[i][0] == 0:
        modified_match_data = match_data
        modified_match_data[i][0] = 1
        result.append(calculate_mmr(modified_match_data, m))
        modified_match_data[i][0] = 0
print(max(result))
