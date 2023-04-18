n = int(input())
summ = 0
summ2 = 0
summ3 = 0
while n > 0:
    summ += n % 10
    n //= 10
    while summ > 9:
        summ2 += summ % 10
        summ //= 10
        while summ2 > 9:
            summ3 += summ2 % 10
            summ2 //= 10
print (summ + summ2 + summ3)

# решение со вложенными циклами не получактся с числом 98998989844648944949494 - выходит 15

#number = int(input())
#while number > 9:
    #total = 0
	#while number != 0:
        #total += number % 10
	    #number //= 10
	#number = total
#print(number)
