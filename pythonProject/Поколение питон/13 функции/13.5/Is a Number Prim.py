# объявление функции
def is_prime(num):
    p = 0
    for i in range(1, num+1):
        if num % i == 0:
            p += 1
    if p == 2:
        return True
    else:
        return False
# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))