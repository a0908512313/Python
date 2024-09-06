n = input("")
start = "AUG"
end = ["UAA","UAG","UGA"]
result = 0
for i in range(n-3):
    temp = str()
    temp+=n[i]+n[i+1]+n[i+2]
    if temp == start:
        result += 1
        i += 3
        while temp != start:
            i += 3
            temp+=n[i]+n[i+1]+n[i+2]
            for j in end:
                if temp == j:
                    break
print(result)
