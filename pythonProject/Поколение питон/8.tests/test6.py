n = int(input())
count_of_3 = 0
last_digit = n % 10
digit = 0
count_of_last_digit = 0
count_of_evens = 0
sum_of_digit_large_5 = 0
product_of_digit_large_7 = 1
count_of_0_and_5 = 0
while n > 0:
    digit = n % 10
    if digit == 3:
        count_of_3 += 1
    if digit == last_digit:
        count_of_last_digit += 1
    if digit % 2 == 0:
        count_of_evens += 1
    if digit > 5:
        sum_of_digit_large_5 += digit
    if digit > 7:
        product_of_digit_large_7 *= digit
    if digit == 0 or digit == 5:
        count_of_0_and_5 += 1
    n //= 10
print(count_of_3, count_of_last_digit, count_of_evens, sum_of_digit_large_5, product_of_digit_large_7, count_of_0_and_5, sep = '\n')
