n = int(input())
data = list()
for _ in range(n):
    temp = list(input().split())
    data.append(temp)
DATA = dict()
result = 0
score = {"A+": 4.3, "A": 4.0, "A-": 3.7,
         "B+": 3.3, "B": 3.0, "B-": 2.7,
         "C+": 2.3, "C": 2.0, "C-": 1.7,
         "D": 1.0, "E": 0, "X": 0}
for i in data:
    lesson = i[0]
    level = i[1]
    DATA[lesson] = level

for i in DATA.values():
    result += score[i]

print(result)
