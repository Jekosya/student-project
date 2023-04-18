# объявление функции
def is_palindrome(text):
    abc = []
    for c in text:
        if c.isalpha():
            abc.append(c.lower())
    part_1 = abc[:len(abc)//2 + 1]
    part_2 = abc[:len(abc)//2:-1]
    for i in range  (len(part_2)):
        if part_1[i] != part_2[i]:
            return False

    return True
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))