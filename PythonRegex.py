import re
pattern=re.compile(r'')

def validPassword2(password):
    flag = 0

    while True:
        if not (8 <= len(password) <= 15): # Length of Password is 8-15 Characters
            flag = -1
            break
        elif re.search(r'[!$*&@#+=)/(]', password) is None: # Password includes special characters
            flag = -1
            break
        elif re.search(r'[A-Z]', password) is None: # Password includes Uppercase letters
            flag = -1
            break
        elif re.match(r'^[!$*&@#+=)/(]', password): # Password starts with special characters
            flag = -1
            break
        else:
            flag = 0
            break

    return flag
