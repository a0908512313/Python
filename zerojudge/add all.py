INPUT = list()
while True:
    n = int(input())
    if n == 0:
        break
    temp = list(map(int, input().split()))
    temp.sort()
    INPUT.append((n, temp))

for n, nums in INPUT:
    result = 0
    while len(nums) > 1:
        first = nums[0]
        second = nums[1]
        result += (first+second)
        nums = nums[2:]
        nums.append(first+second)
        nums.sort()

    print(result)
