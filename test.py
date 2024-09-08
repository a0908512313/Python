n = input("")
code = [n[i:i+3] for i in range(0, len(n), 3)]
start = "AUG"
end = {"UAA", "UAG", "UGA"}
result = 0
i = 0
while i < len(code):
    if code[i] == start:
        result += 1
        i += 1
        while i < len(code) and code[i] not in end:
            i += 1
            result += 1
        if code[i] in end and i < len(code):
            i += 1
    else:
        i += 1
print(result)
