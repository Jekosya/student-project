abc = []
res = []
ser = []
for _ in range(int(input())):
    abc.append(input())
for k in range(int(input())):
    s = input()
        ser.append(s)
for i in ser:
    for j in abc:
        if i.lower() in j.lower():
            res.append(j)
print(*res, sep="\n")



