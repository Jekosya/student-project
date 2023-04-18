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
def get_next_prime(num):
    for i in range (num, 2147483647):
        if i > num and is_prime(i):
            return i


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))