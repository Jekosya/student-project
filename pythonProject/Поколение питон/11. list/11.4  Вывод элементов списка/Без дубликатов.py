abc = []
for _ in range(int(input())):
    s = input()
    if s not in abc:
        abc.append(s)
print(*abc, sep='\n')
