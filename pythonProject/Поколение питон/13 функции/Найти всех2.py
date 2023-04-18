# объявление функции
def find_all(target, symbol):
    pos = [i for i in range (len(target)) if target[i] in symbol]
    return pos

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))