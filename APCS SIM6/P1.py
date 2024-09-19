number, defaultPrice = list(map(int, input().split()))
age = [int(i) for i in input().split()]
couponCount = int(input())
left, right, price = [0]*couponCount, [0]*couponCount, [0]*couponCount
total = 0
for i in range(couponCount):
        left[i], right[i], price[i] = list(map(int, input().split()))
        
for i in range(number):
    for j in range(couponCount):
        if age[i] >= left[j] and age[i] <= right[j]:
                total += price[j]
        else:
                total += defaultPrice
print(total)
