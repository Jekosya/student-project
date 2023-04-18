l = []
for _ in range(int(input())):
    n = int(input())
    l.append(n)
del l[l.index(max(l))]
del l[l.index(min(l))]
print(*l, sep='\n')



