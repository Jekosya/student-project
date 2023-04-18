from math import *
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Нет корней')
        quit()
    if d == 0:
        return (-b + sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
    t = (min((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)), max((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)))
    return t


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)