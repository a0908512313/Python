def is_palindrome(num):
    return str(num) == str(num)[::-1]


def nth_palindrome(n):
    count = 0
    num = 0
    while count < n:
        if is_palindrome(num):
            count += 1
        num += 1
    return num - 1


n = int(input())
print(nth_palindrome(n))
