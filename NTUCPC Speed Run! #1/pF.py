correct_len = int(input())
correct = input().split()
n = int(input())
cases = list()
for _ in range(n):
    temp = input().split()
    temp[0] = int(temp[0])
    cases.append(temp)

for case in cases:
    if case[0] != correct_len:
        print("No")
    else:
        answer = case[1:]
        if len(answer) != correct_len:
            print("No")
        else:
            test = len(answer) == len(correct) and \
                all(answer.count(word) == correct.count(word)
                    for word in set(answer))
            print("Yes" if test else "No")
