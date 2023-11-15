import re
pattern=re.compile(r'')

def validPassword2(password):
    flag = 0

    while True:
        if not (8 <= len(password) <= 15): # Length of Password is 8-15 Characters
            flag = -1
            break
        elif re.search(r'[!$*&@#+=]', password) is None: # Password includes special characters
            flag = -1
            break
        elif re.search(r'\d', password) is None: # Password includes numbers or digits
            flag = -1
            break
        elif re.search(r'[A-Z]', password) is None: # Password includes Uppercase letters
            flag = -1
            break
        elif re.search(r'[a-z]', password) is None: # Password includes Lowercase letters
            flag = -1
            break
        elif re.search(r'^[!$*&@#+=]', password): # Password doesn't start with special characters
            flag = -1
            break
        else:
            flag = 0
            return flag

    if flag == -1:
     return flag
