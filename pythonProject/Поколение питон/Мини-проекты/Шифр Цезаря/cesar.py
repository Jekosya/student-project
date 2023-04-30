ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
en = 'abcdefghijklmnopqrstuvwxyz'
def hide_RU(s):
    ent = ""
    for c in range(len(s)):
        if s[c] == " ":
            x = ord(" ")
        else:
            x = ord(s[c].lower()) + step
            if x > 1103:
                x = 1071 + (x - 1103)
        ent += chr(x)
    return ent

def hide_ENG(s):
    ent = ""
    for c in range(len(s)):
        if s[c] == " ":
            x = ord(" ")
        else:
            x = ord(s[c].lower()) + step
            if x > 122:
                x = 97 + (x - 123)
        ent += chr(x)
    return ent

def unhide_RU(s):
    ent = ""
    for c in range(len(s)):
        if s[c] == " ":
            x = ord(" ")
        else:
            x = ord(s[c].lower()) - step
            if x < 1072:
                x = 1104 - (1072 - x)
        ent += chr(x)
    return ent

def uhide_ENG(s):
    ent = ""
    for c in range(len(s)):
        if s[c] == " ":
            x = ord(" ")
        else:
            x = ord(s[c].lower()) - step
            if x < 97:
                x = 123 - (97 - x)
        ent += chr(x)
    return ent

while True:
    coding = input('Вы хотите зашифровать и расшифровать текст? Выберите "1" или "2"\n1 – зашифровать\n2 – расшифровать \n')
    if coding != "1" and coding != "2":
        print('Вы ввели неверное значение.')
    else:
        break

while True:
    language = input('Для выбора языка введите "рус" или "eng" \n')
    if language != "рус" and language != "eng":
        print('Вы ввели неверное значение.')
    else:
        break

while True:
    if language == "рус":
        step = int(input('Введите шаг сдвига шифра от 1 до 32 по количеству букв в русском алфавите (буква Ё не учитывается)\n'))
        if 0 < step > 32:
            print('Вы ввели неверное значение.')
        else:
            break

    if language == "eng":
        step = int(input('Введите шаг сдвига шифра от 1 до 26 по количеству букв в английском алфавите\n'))
        if 0 < step > 26:
            print('Вы ввели неверное значение.')
        else:
            break
while True:
    abc = input('Введите текст\n')

    if language == 'рус' and coding == "2":
        print (unhide_RU(abc))
    if language == 'рус' and coding == "1":
        print (hide_RU(abc))
    if language == 'eng' and coding == "2":
        print (uhide_ENG(abc))
    if language == 'eng' and coding == "1":
        print (hide_ENG(abc))
    exxt = input('Для повтора нажмите "Д". Чтобы ВЫЙТИ нажмите любую другую кнопку')
    if exxt != 'Д':
       break