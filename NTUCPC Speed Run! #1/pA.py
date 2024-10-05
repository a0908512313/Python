x, y, z = map(int, input().split())
t = x + y
c = z // t
temp = z % t
result = c * x
result += min(temp, x)
print(result)
