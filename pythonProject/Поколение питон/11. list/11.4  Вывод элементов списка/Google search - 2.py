abc = []
ser = []
for _ in range(int(input())):
    abc.append(input())
for k in range(int(input())):
    ser.append(input())
for i in ser:
    for j in abc[::-1]:
        if i.lower() not in j.lower():
            del(abc[abc.index(j)])
print(*abc, sep="\n")