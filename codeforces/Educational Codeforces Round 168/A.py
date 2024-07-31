def calculate_typing_time(s):
    time = 2  # time for the first character
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            time += 1
        else:
            time += 2
    return time


def find_max_typing_time(s):
    max_time = 0
    best_string = ""

    for i in range(len(s) + 1):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new_string = s[:i] + c + s[i:]
            new_time = calculate_typing_time(new_string)
            if new_time > max_time:
                max_time = new_time
                best_string = new_string

    return best_string


# Read number of test cases
t = int(input())
results = []

for _ in range(t):
    s = input().strip()
    results.append(find_max_typing_time(s))

# Print results
for result in results:
    print(result)
