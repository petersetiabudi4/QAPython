import re
pattern=re.compile(r'')

def validPassword2(password):
    flag = 0

    while True:
        if not (8 <= len(password) <= 15):
            flag = -1
            break
        elif re.search(r'[!$*&@#+=]', password) is None:
            flag = -1
            break
        elif re.search(r'\d', password) is None:
            flag = -1
            break
        elif re.search(r'[A-Z]', password) is None:
            flag = -1
            break
        elif re.search(r'[a-z]', password) is None:
            flag = -1
            break
        elif re.search(r'^[!$*&@#+=]', password):
            flag = -1
            break
        else:
            flag = 0
            return flag

    if flag == -1:
     return flag
