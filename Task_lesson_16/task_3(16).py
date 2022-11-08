# Check password requirements

import re


def check_password_format():
    user_password = input('Enter your password: ')
    total = (len(user_password) >= 8,
             re.search(r'[a-z]', user_password),
             re.search(r'[A-Z]', user_password),
             re.search(r'[0-9]', user_password),
             re.search(r'[d_$#@+=-]', user_password))
    if len(user_password) < 8:
        return 'Minimum password length must be 8 characters'
    if re.search(r'[a-z]', user_password) is None:
        return 'At least 1 letter must be lowercase'
    if re.search(r'[A-Z]', user_password) is None:
        return 'At least 1 letter must be uppercase'
    if re.search(r'[0-9]', user_password) is None:
        return 'Password must contain at least one number'
    if re.search(r'[d_$#@+=-]', user_password) is None:
        return 'Password must contain at least one of this characters: $, #, @, -, +, ='
    if all(total) is True:
        return "Password is correct"


print(check_password_format())
