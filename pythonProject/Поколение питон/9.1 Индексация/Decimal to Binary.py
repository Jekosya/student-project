n = int(input())
s = ''
while n > 0:
    s += str(n % 2)
    n //= 2
for c in range(len(s)-1, -1, -1):
    print(s[c], end='')
