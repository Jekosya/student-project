min = []
zer = []
pls = []
for _ in range(int(input())):
    n = int(input())
    if n < 0:
        min.append(n)
    elif n == 0:
        zer.append(n)
    else:
        pls.append(n)
print(*min,*zer,*pls, sep = "\n")