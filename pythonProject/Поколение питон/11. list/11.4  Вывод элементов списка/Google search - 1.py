abc = []
res = []
for _ in range(int(input())):
    abc.append(input())
ser = input().lower()
for i in abc:
    if ser in i.lower():
        res.append(i)
print(*res, sep="\n")



