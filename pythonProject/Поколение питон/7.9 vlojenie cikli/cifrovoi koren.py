n = int(input())
summ = 0
summ2 = 0
summ3 = 0
while n > 0:
    summ += n % 10
    n //= 10
while summ > 0:
    summ2 += summ % 10
    summ //= 10
while summ2 > 0:
    summ3 += summ2 % 10
    summ2 //= 10
print(summ+summ2+summ3)