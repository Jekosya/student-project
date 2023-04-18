import random
print("Добро пожаловать в числовую угадайку")
y = int(input('Введите максимальное число, которое может быть загадано \n'))
x = random.randint(1, y)
def is_valid(s):
    if s.isdigit() == True and 0 < int(s) < y:
        return True
    else:
        return False
cnt = 0
while True:
    num = input(f'Введите число от 1 до {y} \n')
    cnt += 1
    if is_valid(num) == False:
        print('А может быть все-таки введем целое число от 1 до', y, '\n')
        continue
    elif int (num) < x:
        print('Ваше число меньше загаданного, попробуйте еще разок \n')
    elif int (num) > x:
        print('Ваше число больше загаданного, попробуйте еще разок \n')
    else:
        print('Вы угадали, поздравляем! \n')
        print('Ввм потребовалось', cnt, 'попыток', '\n')
        print('Хотите сыграть еще? Введите "y" \n')
        if input() == 'y':
            x = random.randint(1, int(input('Введите максимальное число, которое может быть загадано \n')))
            continue
        else:
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')