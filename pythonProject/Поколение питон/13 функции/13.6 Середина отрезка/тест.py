from math import sqrt
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
    quit()
x1 = (-b + sqrt(d)) / (2 * a)
x2 = (-b - sqrt(d)) / (2 * a)
if d == 0:
    print(x1)
else:
    print(min(x1, x2), max(x1, x2), sep = '\n')