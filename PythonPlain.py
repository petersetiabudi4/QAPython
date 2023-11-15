def validPassword1(s):
    capital_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabets = "abcdefghijklmnopqrstuvwxyz"
    special_chars = "!$*&@#+=)/("
    numbers = "0123456789"

    l, u, p, n = 0, 0, 0, 0 # l = lowercase, u = Uppercase, p = special character, n = numbers

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

    #Compile every aspect with the additional metric that the password doesn't start with special character.
    return u >= 1 and p >= 1 and l + p + u + n == len(s) and not any(s.startswith(char) for char in special_chars)

