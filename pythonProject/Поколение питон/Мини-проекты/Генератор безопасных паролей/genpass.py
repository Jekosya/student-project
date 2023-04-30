import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
while True:
    cnt = input('Количество паролей для генерации \n')
    ln = input('Длина одного пароля \n')
    dig = input('Включать ли цифры 0123456789? да или нет? \n')
    UP = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да или нет? \n')
    LOW = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да или нет? \n')
    spec = input('Включать ли символы !#$%&*+-=?@^_? да или нет? \n')
    susp = input('Исключать ли неоднозначные символы il1Lo0O? да или нет? \n')

    if dig == 'да':
        chars += digits
    if UP == 'да':
        chars += uppercase_letters
    if LOW == 'да':
        chars += lowercase_letters
    if spec == 'да':
        chars += punctuation
    if susp == 'да':
        for c in 'il1Lo0O':
            chars = chars.replace(c, "")


    def generate_password(length):
        chr = ''
        for i in range(int(length)):
            chr += random.choice(chars)
        return chr


    for i in range(int(cnt)):
        print(generate_password(ln))
    rep = input('Хотите сгенерировать еще пароли? Тогда нажмите "Y" \nДля выхода нажмите любую другую клавишу\n').lower()
    if rep != "y" and rep != "н":
        break

