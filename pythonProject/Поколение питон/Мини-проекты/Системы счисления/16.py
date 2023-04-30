n = int(input())
x = []
y = ''
while n > 1:
    x.append(int(n % 16))
    n = n/16
    if n == 1:
        x.append(1)
for c in x:
    if c == 10:
        c = 'A'
    elif c == 11:
        c = 'B'
    elif c == 12:
        c = 'C'
    elif c == 13:
        c = 'D'
    elif c == 14:
        c = 'E'
    elif c == 15:
        c = 'F'
    y += str(c)
print (y[::-1])