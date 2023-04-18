n = int(input())
xlist = []
y = []
for _ in range(n):
    x = int(input())
    xlist.append(x)
    y.append(x ** 2 + 2 * x + 1)
print(*xlist, sep='\n')
print()
print(*y, sep='\n')




