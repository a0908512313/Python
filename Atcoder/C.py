from itertools import permutations

n, k = map(int, input().split())
s = input()


def is_palindrome(s):
    return s == s[::-1]


def has_palindrome_substring(s, K):
    for i in range(len(s) - K + 1):
        if is_palindrome(s[i:i+K]):
            return True
    return False


def count_valid_permutations(S, K):
    valid_count = 0
    seen_permutations = set()

    def backtrack(path, chars):
        nonlocal valid_count
        if len(path) == len(S):
            perm_str = ''.join(path)
            if perm_str not in seen_permutations:
                seen_permutations.add(perm_str)
                if not has_palindrome_substring(perm_str, K):
                    valid_count += 1
            return

        for i in range(len(chars)):
            next_path = path + [chars[i]]
            next_chars = chars[:i] + chars[i+1:]
            backtrack(next_path, next_chars)

    backtrack([], list(S))
    return valid_count


print(count_valid_permutations(s, k))
