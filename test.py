n = int(input())
test = list()
for _ in range(n):
    test.append(list(map(int, input().split())))
data = [[734, 0, 4, 8, 6, 12, 5],
        [632, 4, 1, 9, 6, 8, 8],
        [8, 11, 2, 3, 5, 9, 17],
        [612, 5, 4, 6, 7, 4, 20],
        [302, 4, 11, 88, 8, 0, 45]]
result = list()


def testA(TEST):
    for i in range(n):
        for a in range(5):
            for b in range(1, 5):
                if test[i][0] == data[a][b]:
                    return test[a][b], test[a][-1]


def testB(TEST):
    for i in range(n):
        for a in range(5):
            for b in range(1, 5):
                if test[i][1] == data[a][b]:
                    return test[a][b], test[a][-1]
