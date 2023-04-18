l = input().split()
m = input().split()
maxl = 0
dif = abs(len(l) - len(m))
if len(l) > len(m):
    maxl = len(l)
    for _ in range(dif):
        m.append(0)
elif len(l) < len(m):
    maxl = len(m)
    for _ in range(dif):
        l.append(0)
else:
    maxl = len(l)
sum = []
for i in range(maxl):
    sum.append(int(l[i]) + int(m[i]))
print(*sum)