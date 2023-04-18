a = int(input())
b = int(input())
summ = 0
largest = 0
capacious = 0
for i in range(a, b + 1):
    for j in range(1, i+1):
        if i % j == 0:
            summ += j
        if summ >= largest:
            largest = summ
            capacious = i
    summ = 0
print(capacious, largest)