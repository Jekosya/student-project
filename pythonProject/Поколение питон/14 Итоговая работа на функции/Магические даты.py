def is_magic(date):
    date = date.split('.')
    return int(date[0]) * int(date[1]) == int(date[2][2:])
date = input()
print(is_magic(date))