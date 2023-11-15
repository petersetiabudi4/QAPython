s = "P$eter404"
capital_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabets = "abcdefghijklmnopqrstuvwxyz"
special_chars = "!$*&@#+=)"
numbers = "0123456789"

l, u, p, n = 0, 0, 0, 0

if 8 <= len(s) <= 15:
    for i in s:
        # counting lowercase alphabets
        if i in small_alphabets:
            l += 1

        # counting uppercase alphabets
        if i in capital_alphabets:
            u += 1

        # counting numbers
        if i in numbers:
            n += 1

        # counting the mentioned special characters
        if i in special_chars:
            p += 1

if l >= 1 and u >= 1 and p >= 1 and n >= 1 and l + p + u + n == len(s) and not s.startswith(tuple(special_chars)):
    print("Valid Password")
else:
    print("Invalid Password")