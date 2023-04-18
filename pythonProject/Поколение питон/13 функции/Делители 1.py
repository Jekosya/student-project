# объявление функции
def get_factors(num):
    n = []
    for i in range (1, num+1):
        if num % i == 0:
            n.append(i)
    return n
# считываем данные
n = int(input())
# вызываем функцию
print(get_factors(n))