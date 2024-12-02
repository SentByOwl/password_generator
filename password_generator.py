from secrets import randbelow
import re

"""
This script generates a 60 character long unique password
and ensures that it includes numbers and special characters
"""

pool = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H',
    'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',
    'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W',
    'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
    '9', '0', '!', '@', '#', '$', '%', '&', '*', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*'
]

patt2 = re.compile(r"[0-9]{5,}")
patt3 = re.compile(r"[a-z]{3,}")
patt4 = re.compile(r"[A-Z]{3,}")
special_chars = ['!', '@', '#', '$', '%', '&', '*']

def create_password(password_chars_list: list) -> list:
    count = 60
    while count > 0:
        password_chars_list.append(pool[randbelow(len(pool))])
        count -= 1
    return password_chars_list

def check_special_chars(special_chars: list, password_string: str) -> bool:
    pass_check = True
    for i in special_chars:
        if i not in password_string:
            pass_check = False
    return pass_check

while True:
    password_chars_list = []
    password_string = ''.join([i for i in create_password(password_chars_list)])

    if not check_special_chars(special_chars, password_string):
        continue

    if not re.search(patt2, password_string):
        continue

    if not re.search(patt3, password_string):
        continue

    if not re.search(patt4, password_string):
        continue

    else:
        print(f"\nPassword: {password_string}\n")
        break
