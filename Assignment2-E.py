def palindrome(a):
    n = str(a)
    r = n[::-1]
    if n == r:
        return True
    return False

print(palindrome(767))
