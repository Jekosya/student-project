# объявление функции
def is_password_good(password):
    flagU = False
    flagL = False
    flagD = False
    for i in password:
        if i.isupper() == True:
            flagU = True
        if i.islower() == True:
            flagL = True
        if i.isdigit() == True:
            flagD = True
    if flagU and flagL and flagD and len(password) > 7:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))