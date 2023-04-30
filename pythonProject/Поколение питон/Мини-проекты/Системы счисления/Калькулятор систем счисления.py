
def SIXTEEN(num):
    x = []
    y = ''
    while num > 1:
        x.append(int(num % 16))
        num = num / 16
        if num == 1:
            x.append(1)
    for c in x:
        if c == 10:
            c = 'A'
        elif c == 11:
            c = 'B'
        elif c == 12:
            c = 'C'
        elif c == 13:
            c = 'D'
        elif c == 14:
            c = 'E'
        elif c == 15:
            c = 'F'
        y += str(c)
    return y[::-1]

def DUAL(num):
    y = ''
    while num > 1:
        y += str(int(num % 2))
        num = num / 2
        if num == 1:
            y += '1'

    return y[::-1]



choice = ''
while True:
    choice = input("Введите систему счисления, в которую хоите перевести число: 2, 16\n")
    if choice == '2' or choice == '16':
        break
    else:
        print('Вы ввели неверное значение')

if choice == '16':
    n = int(input('Введите число \n'))
    print(SIXTEEN(n))

if choice == '2':
    n = int(input('Введите число \n'))
    if n == 1:
        print(n)
    else:
        print(DUAL(n))
