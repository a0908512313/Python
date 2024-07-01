n, a, x, y = map(int, input().split())
price = 0
if n <= a:
  price+=x*n
else:
  price = x*a + (n-a) * y
print(price)
