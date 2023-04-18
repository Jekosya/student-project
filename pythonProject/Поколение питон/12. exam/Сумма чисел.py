n = input().split()
sum = 0
for i in range(len(n)):
    sum += int(n[i])
print(*n, sep='+', end='')
print( '=', sum, sep='')