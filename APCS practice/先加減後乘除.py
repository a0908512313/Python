def nof(s):
    temp = s.split("*")
    for i in range(len(temp)):
        temp[i] = eval(temp[i])
    result = "*".join(map(str, temp))
    return eval(result)

s=  input()

if "f" not in s:
    ans = nof(s)
    print(ans)
else:
    
