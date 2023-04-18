def is_miror(s):
    if s[:len(s) // 2] in s[-1 :len(s) // 2 - 1: -1]:
        return True
    else:
        return False
def is_prime(num):
    p = 0
    for i in range(1, num+1):
        if num % i == 0:
            p += 1
    if p == 2:
        return True
    else:
        return False
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def is_valid_password(password):
    return is_miror(password[0]) and is_prime(int(password[1])) and is_even(int(password[2])) and len(password) == 3
psw = input().split(':')
print(is_valid_password(psw))