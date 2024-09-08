n = input("")
start = "AUG"
end = ("UAA", "UAG", "UGA")
result = 0
i = 0
while i <= len(n) - 3:
    temp = str()
    temp += n[i]+n[i+1]+n[i+2]
    if temp == start:
        result += 1
        i += 3
        temp += n[i]+n[i+1]+n[i+2]
        while temp not in end:
            i += 3
            temp += n[i]+n[i+1]+n[i+2]
            result += 1
    else:
        i += 1
print(result)
