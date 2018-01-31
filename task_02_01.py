def is_palindrome(s):
    s = str(s).lower()
    b = list(''.join(s))
    while ' ' in b:
        b.remove(' ')
    b1 = list(reversed(b))
    return True if b == b1 else False