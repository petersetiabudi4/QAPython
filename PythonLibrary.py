# Python program to check validation of password
# Module of regular expression is used with search()
import re

password = "P$eter404"
flag = 0

while True:
    if not (8 <= len(password) <= 15):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[!$*&@#+=]", password):
        flag = -1
        break
    elif re.search("^[!$*&@#+=]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")
