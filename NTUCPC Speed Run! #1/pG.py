data = [list(input()) for _ in range(2)]
data.sort(reverse=True, key=len)
a, b = data
result = ""
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            length = 0
            while j + length < len(b) and a[i + length] == b[j + length]:
                length += 1
            if length > len(result):
                result = ''.join(a[i:i + length])

if not result:
    print("No")
else:
    print("Yes")
    print(result)
