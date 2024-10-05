n = int(input())
events = list()
for _ in range(n):
    events.append(list(input().split()))
teams = ["A", "B", "C", "D", "E", "F"]
data = {team: [0, 0, 0, 0] for team in teams}
for event in events:
    if event[0] == "match":
        data[event[1]][0] += 1
        data[event[1]][1] += 1
        data[event[2]][0] += 1
    elif event[0] == "point":
        def cal(total, win):
            return win/total if win > 0 else 0
        team_avg = list()
        for team in teams:
            avg = cal(data[team][0], data[team][1])
            team_avg.append(avg)
            data[team][-2] = avg
        max_avg = max(team_avg)
        if team_avg.count(max_avg) == 1:
            index = team_avg.index(max_avg)
            data[teams[index]][-1] += 1

result = list()
for team in teams:
    result.append(data[team][-1])
print(' '.join(map(str, result)))
