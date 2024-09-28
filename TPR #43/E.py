def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def max_gcd_after_removal(n, numbers):
    if n <= 3:
        return max(numbers)

    # 計算所有數對的 GCD
    pair_gcds = []
    for i in range(n):
        for j in range(i+1, n):
            pair_gcds.append(gcd(numbers[i], numbers[j]))

    max_gcd = max(pair_gcds)

    # 檢查是否可以通過刪除兩個數字來達到這個 GCD
    for possible_gcd in range(max_gcd, 0, -1):
        count = sum(1 for num in numbers if num % possible_gcd == 0)
        if count >= n - 2:
            return possible_gcd

    return 1


# 讀取輸入
n = int(input())
numbers = list(map(int, input().split()))

# 計算並輸出結果
result = max_gcd_after_removal(n, numbers)
print(result)
